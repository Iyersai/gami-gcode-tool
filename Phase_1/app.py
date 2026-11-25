import json
import os
import tempfile

import streamlit as st  # the web page library
from gscrib import GCodeBuilder  # the G-code writer

import gcode_engine as ge  # our own engine: plan -> G-code (gcode_engine.py must be in the same folder)

# 1. Page setup
LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gami_logo.png")
st.set_page_config(page_title="GAMI G-Code Tool", page_icon=LOGO_PATH, layout="wide")

# White background (also set in .streamlit/config.toml) and a slimmer top gap
st.markdown(
    """
    <style>
    .stApp, [data-testid="stHeader"] { background-color: #FFFFFF; }
    .block-container { padding-top: 1.5rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header: GAMI logo on the left, title beside it, options below
logo_col, title_col = st.columns([1, 5], vertical_alignment="center")
with logo_col:
    st.image(LOGO_PATH, width=190)
with title_col:
    st.markdown(
        "<h1 style='margin:0; color:#00A685;'>G-Code Generator</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "Upload **plan_ops.json** (made by `plan_reader.py` from Oskar's CAPP project) "
        "and generate G-code for one machine."
    )
st.divider()

col1, col2 = st.columns(2)

plan = None
machine_id = None
settings = {}

# 2. Left column: input and machine settings
with col1:
    st.header("1. Input plan")
    uploaded_file = st.file_uploader("Upload plan_ops.json", type=["json"])

    if uploaded_file is not None:
        plan = json.load(uploaded_file)
        if "machines" not in plan or "stock_bounds_mm" not in plan:
            st.error(
                "This file has the old format. Run the new plan_reader.py again "
                "and upload the new plan_ops.json."
            )
            plan = None
        else:
            st.success(f"Plan loaded: part {plan.get('part_id')}, {len(plan['operations'])} operations")
            with st.expander("View uploaded data"):
                st.json(plan, expanded=False)

    if plan is not None:
        st.header("2. Machine and settings")
        machine_id = st.selectbox("Machine (from the plan)", plan["hosts"])
        info = plan["machines"][machine_id]
        st.caption(
            f"{info.get('model')}, {info.get('axis_count')} axes, "
            f"{len(info['tools'])} of {info.get('tool_capacity')} tool slots used in the plan"
        )

        numbers = ge.tool_numbers(plan, machine_id)
        rows = []
        for op in plan["operations"]:
            rows.append(
                {
                    "Seq": op["sequence_index"],
                    "Operation": f"{op['op_id']} {op['entity']}",
                    "Tool": op["tool_id"],
                    "T number": numbers.get(op["tool_id"], "NOT IN MAGAZINE"),
                    "rpm": round(op["spindle_rpm"]),
                    "feed mm/min": round(op["feed_mm_min"], 1),
                }
            )
        st.dataframe(rows, hide_index=True)

        settings["tool_change"] = st.text_input("Tool change format", ge.DEFAULT_SETTINGS["tool_change"])
        settings["program_end"] = st.selectbox("Program end code", ["M30", "M2"])
        settings["safe_margin_mm"] = st.number_input(
            "Safe height above the highest planned point (mm)", min_value=1.0, value=5.0, step=1.0
        )

        st.info(
            "**Assumptions**\n\n"
            "1. Machine X = part x, machine Y = -(part z), machine Z = part y minus the top of the raw stock "
            "(the plan's tool axis +Y becomes the spindle axis).\n"
            "2. G54 is at the stock corner (x = 0, z = 0) on the top face of the raw stock.\n"
            "3. T number = position in the machine magazine list (resident tools first, then newly loaded tools).\n"
            "4. Cutting and linking moves run at the planned feed rate."
        )

# 3. Right column: generate and show the output
with col2:
    st.header("3. Generated output")
    if plan is not None:
        if st.button("Generate G-Code", type="primary"):
            problems = ge.validate(plan, machine_id)
            if "{tool}" not in settings["tool_change"]:
                problems.append("The tool change format must contain {tool}.")
            if problems:
                st.session_state["result"] = {"problems": problems, "key": (uploaded_file.name, machine_id)}
            else:
                out_path = os.path.join(tempfile.mkdtemp(), "output.nc")
                g = GCodeBuilder(output=out_path, print_lines=False)
                stats = ge.generate(plan, machine_id, g, settings)
                with open(out_path, "r", encoding="utf-8") as f:
                    gcode_text = f.read()
                st.session_state["result"] = {
                    "key": (uploaded_file.name, machine_id),
                    "gcode": gcode_text,
                    "stats": stats,
                    "file_name": f"{plan.get('part_id')}_{machine_id}.nc",
                }

        result = st.session_state.get("result")
        if result and result["key"] == (uploaded_file.name, machine_id):
            if "problems" in result:
                for p in result["problems"]:
                    st.error(p)
            else:
                stats = result["stats"]
                st.success(f"G-code generated for {machine_id}. It is NOT verified yet: check it in CAMotics.")

                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Operations", stats["operations"])
                c2.metric("Tool changes", stats["tool_changes"])
                c3.metric("Feed moves", stats["feed_moves"])
                c4.metric("Safe Z (mm)", stats["safe_z"])

                bb = stats["bbox"]
                st.caption(
                    "Machine coordinates used (mm): "
                    f"X {bb['X'][0]} to {bb['X'][1]}, Y {bb['Y'][0]} to {bb['Y'][1]}, Z {bb['Z'][0]} to {bb['Z'][1]}"
                )

                # warn if the program cuts below the bottom of the stock
                bounds = plan["stock_bounds_mm"]
                bottom_z = bounds["min"][1] - bounds["max"][1]
                if bb["Z"][0] < bottom_z - 0.001:
                    st.warning(
                        f"The program goes {bottom_z - bb['Z'][0]:.1f} mm below the bottom of the stock "
                        f"(Z {bottom_z:g}). This is the drill point leaving a through hole. "
                        "Make sure the fixture or parallels allow it."
                    )

                st.text_area("G-Code Preview", result["gcode"], height=400)
                st.download_button(
                    label="Download G-Code File (.nc)",
                    data=result["gcode"],
                    file_name=result["file_name"],
                    mime="text/plain",
                )
    else:
        st.write("Upload a plan on the left to start.")