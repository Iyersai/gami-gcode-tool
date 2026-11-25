"""Join Oskar's production plan (step D) with the CL data (step B).

Usage:  python plan_reader.py <project_folder>
Prints, for every planned operation in sequence order: tool, direction,
spindle speed, feed, number of path segments and points, and the first point.
Writes plan_ops.json into the project folder: the input of the G-code app.

plan_ops.json contains
  part_id, stock_bounds_mm      from the plan and step_b/stock_selection.json
  hosts                         machines the plan runs on
  machines                      per machine: model, axes, magazine (resident + newly loaded tools)
  operations                    in machining order, with speed, feed and all path points
"""
import json
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "Example_V1")
plan = json.loads((root / "step_d" / "production_plan.json").read_text(encoding="utf-8"))
step_b = json.loads((root / "step_b" / "step_b.json").read_text(encoding="utf-8"))

stock_bounds = None
stock_file = root / "step_b" / "stock_selection.json"
if stock_file.exists():
    sel = json.loads(stock_file.read_text(encoding="utf-8"))
    stock_bounds = sel.get("stock_selection", {}).get("stock_bounds_mm")

# index every step B tool-path artifact by (operation id, TAD id, tool id)
candidates = {}


def collect(op):
    for art in op.get("tool_path_artifacts", []):
        key = (str(art.get("operation_id", op.get("op_id"))), art.get("tad_candidate_id"), art.get("tool_id"))
        candidates[key] = art


for feat in step_b.get("features", []):
    for op in feat.get("step_b", {}).get("operations", []):
        collect(op)
for ent in step_b.get("step_b", {}).get("stock_facing", {}).get("entities", []):
    for op in ent.get("operations", []):
        collect(op)

print(f"{len(candidates)} step B candidates indexed")

hosts = []
out = []
for setup in plan["setups"]:
    for h in setup["hosts"]:
        if h["machine_id"] not in hosts:
            hosts.append(h["machine_id"])
    print(f"\nSetup {setup['setup_id']} on machines {[h['machine_id'] for h in setup['hosts']]}")
    for o in sorted(setup["operations"], key=lambda x: x["sequence_index"]):
        # plan op ids look like "op3"; step B uses "3"
        art = candidates.get((o["op_id"].removeprefix("op"), o["tad_id"], o["tool_id"]))
        if not art:
            print(f"  {o['sequence_index']} {o['op_id']}: NO MATCH for candidate id")
            continue
        segs = art.get("segments", [])
        pts = [p for s in segs for p in s["polyline_mm"]]
        cc = art.get("cutting_conditions", {})
        print(
            f"  {o['sequence_index']} {o['op_id']:<4} {o['entity_id']:<14} {o['operation_role']:<14} "
            f"{o['direction_label']} {o['tool_id']:<22} S={cc.get('spindle_speed_rpm', 0):7.0f} "
            f"F={cc.get('feed_rate_mm_per_min', 0):6.0f} segs={len(segs):3d} pts={len(pts):4d} "
            f"first={pts[0] if pts else None}"
        )
        out.append(
            {
                "sequence_index": o["sequence_index"],
                "op_id": o["op_id"],
                "entity": o["entity_id"],
                "role": o["operation_role"],
                "direction": o["direction_label"],
                "tool_id": o["tool_id"],
                "tool_change_before": o["tool_change_before"],
                "spindle_rpm": cc.get("spindle_speed_rpm"),
                "feed_mm_min": cc.get("feed_rate_mm_per_min"),
                "segments": [
                    {"motion": s["motion_class"], "kind": s["movement_kind"], "points": s["polyline_mm"]}
                    for s in segs
                ],
            }
        )

# magazine of each machine: resident tools first, then the tools the plan loads
machines = {}
for m in plan.get("physical_machines", []):
    tools = list(m.get("resident_tools", []))
    for t in m.get("newly_loaded_tools", []):
        if t not in tools:
            tools.append(t)
    machines[m["machine_id"]] = {
        "model": m.get("model"),
        "axis_count": m.get("axis_count"),
        "tool_capacity": m.get("tool_capacity"),
        "tool_change_time_min": m.get("tool_change_time_min"),
        "tools": tools,
    }

result = {
    "part_id": plan.get("project", {}).get("part_id"),
    "stock_bounds_mm": stock_bounds,
    "hosts": hosts,
    "machines": machines,
    "operations": out,
}
(root / "plan_ops.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
print("\nWrote plan_ops.json with", len(out), "operations and", len(machines), "machines")