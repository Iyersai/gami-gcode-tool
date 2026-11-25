"""G-code engine: turns plan_ops.json (made by plan_reader.py) into G-code for ONE machine.

The engine contains no AI. The same plan and the same settings always give the same G-code.
`g` is a gscrib GCodeBuilder (anything with write, rapid, move and teardown works).

ASSUMPTIONS that must be confirmed with Oskar / the supervisor (they are printed in the G-code header):
  1. Part to machine axes:  X = part x,  Y = -(part z),  Z = (part y) - (top of the raw stock).
     This is a proper rotation (no mirroring). The tool axis of the plan (+Y) becomes the spindle axis (Z).
     G54 sits at the stock corner x = 0, z = 0, on the top face of the RAW stock.
  2. Tool number T = position in the machine magazine list (resident tools first, then newly loaded tools).
  3. Cutting and linking moves run at the planned feed rate. Rapid moves use G0.
"""

DEFAULT_SETTINGS = {
    "preamble": ["G17 G90", "G21", "G54"],
    "tool_change": "T{tool} M6",
    "spindle_on": "S{speed} M3",
    "spindle_off": "M5",
    "program_end": "M30",
    "safe_margin_mm": 5.0,
}

RAPID = {"rapid"}
FEED = {"cutting", "linking"}


def tool_numbers(plan, machine_id):
    """T number of every tool in the magazine of the machine (starts at 1)."""
    tools = plan["machines"][machine_id]["tools"]
    return {tool: i + 1 for i, tool in enumerate(tools)}


def _clean(v):
    r = round(float(v), 3)
    return 0.0 if r == 0 else r


def to_machine(p, y_top):
    x, y, z = p
    return (_clean(x), _clean(-z), _clean(y - y_top))


def _y_top(plan):
    bounds = plan.get("stock_bounds_mm")
    if not bounds:
        raise ValueError("plan has no stock_bounds_mm: run the new plan_reader.py again")
    return bounds["max"][1]


def validate(plan, machine_id):
    """Return a list of error messages. An empty list means the plan can be generated."""
    errors = []
    if not plan.get("operations"):
        errors.append("The plan has no operations.")
        return errors
    if machine_id not in plan.get("machines", {}):
        errors.append(f"Machine {machine_id} is not in the plan.")
        return errors
    if not plan.get("stock_bounds_mm"):
        errors.append("No stock_bounds_mm in the plan: run the new plan_reader.py again.")
    numbers = tool_numbers(plan, machine_id)
    for op in plan["operations"]:
        label = f"{op['op_id']} ({op['entity']})"
        if op["tool_id"] not in numbers:
            errors.append(f"{label}: tool {op['tool_id']} is not in the magazine of {machine_id}.")
        if op.get("direction") != "+Y":
            errors.append(f"{label}: tool direction {op.get('direction')} is not supported yet (only +Y).")
        if not op.get("spindle_rpm") or op["spindle_rpm"] <= 0:
            errors.append(f"{label}: no valid spindle speed.")
        if not op.get("feed_mm_min") or op["feed_mm_min"] <= 0:
            errors.append(f"{label}: no valid feed rate.")
        if not op.get("segments"):
            errors.append(f"{label}: no toolpath segments.")
        for seg in op.get("segments", []):
            if seg["motion"] not in RAPID | FEED:
                errors.append(f"{label}: unknown motion class '{seg['motion']}'.")
                break
    return errors


def _comment(text):
    return "(" + str(text).replace("(", "[").replace(")", "]") + ")"


def generate(plan, machine_id, g, settings=None):
    """Write the program for one machine into the builder g. Returns a dictionary of statistics."""
    s = dict(DEFAULT_SETTINGS)
    s.update(settings or {})
    errors = validate(plan, machine_id)
    if errors:
        raise ValueError("; ".join(errors))

    numbers = tool_numbers(plan, machine_id)
    y_top = _y_top(plan)
    mach = plan["machines"][machine_id]

    # one safe height above everything the plan does
    all_z = [to_machine(p, y_top)[2] for op in plan["operations"] for seg in op["segments"] for p in seg["points"]]
    safe_z = _clean(max(all_z) + s["safe_margin_mm"])

    g.write(_comment(f"Part {plan.get('part_id')} on {machine_id} {mach.get('model')}"))
    g.write(_comment("ASSUMED axes: X = part x, Y = -part z, Z = part y - top of raw stock"))
    g.write(_comment("ASSUMED G54 = stock corner x0 z0, top face of raw stock. Confirm before use"))
    for line in s["preamble"]:
        g.write(line)

    current_tool = None
    current_speed = None
    tool_changes = 0
    moves = {"rapid": 0, "feed": 0}
    xs, ys, zs = [], [], []

    for op in plan["operations"]:
        tool = op["tool_id"]
        speed = int(round(op["spindle_rpm"]))
        feed = round(op["feed_mm_min"], 1)
        g.write(_comment(f"Begin {op['op_id']} {op['entity']} {op['role']} tool {tool}"))
        g.rapid(z=safe_z)
        if tool != current_tool:
            if current_tool is not None:
                g.write(s["spindle_off"])
            g.write(s["tool_change"].format(tool=numbers[tool]))
            tool_changes += 1
            current_tool = tool
            current_speed = None
        if speed != current_speed:
            g.write(s["spindle_on"].format(speed=speed))
            current_speed = speed

        cur = None
        for seg in op["segments"]:
            pts = [to_machine(p, y_top) for p in seg["points"]]
            if cur is None or cur != pts[0]:
                # not yet at the start of this segment: go there at the safe height
                # (at the start of an operation we are already at the safe height)
                if cur is not None:
                    g.rapid(z=safe_z)
                    moves["rapid"] += 1
                g.rapid(x=pts[0][0], y=pts[0][1])
                moves["rapid"] += 1
                if pts[0][2] != safe_z:
                    g.rapid(z=pts[0][2])
                    moves["rapid"] += 1
            for x, y, z in pts[1:]:
                if seg["motion"] in RAPID:
                    g.rapid(x=x, y=y, z=z)
                    moves["rapid"] += 1
                else:
                    g.move(x=x, y=y, z=z, F=feed)
                    moves["feed"] += 1
            for x, y, z in pts:
                xs.append(x)
                ys.append(y)
                zs.append(z)
            cur = pts[-1]

    g.rapid(z=safe_z)
    g.write(s["spindle_off"])
    g.write(s["program_end"])
    g.teardown()

    return {
        "operations": len(plan["operations"]),
        "tool_changes": tool_changes,
        "safe_z": safe_z,
        "rapid_moves": moves["rapid"],
        "feed_moves": moves["feed"],
        "bbox": {"X": (min(xs), max(xs)), "Y": (min(ys), max(ys)), "Z": (min(zs), max(zs))},
        "tool_numbers": numbers,
    }