# GAMI G-Code Generator

A web app that turns a CAPP production plan into G-code for one machine.

## How it works

1. **`plan_reader.py`** joins the production plan (step D) with the tool-path data (step B) of a CAPP project folder and writes `plan_ops.json`.
2. **`app.py`** (Streamlit) lets you upload `plan_ops.json`, choose a machine, adjust settings, and generate G-code.
3. **`gcode_engine.py`** does the work: checks the plan, converts coordinates, and writes the program with [gscrib](https://pypi.org/project/gscrib/).

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Usage

Run these from inside the `Phase_1` folder:

```bash
python plan_reader.py Example_V1   # writes Example_V1/plan_ops.json
streamlit run app.py               # opens the app in the browser
```

Upload `plan_ops.json`, pick the machine, click **Generate G-Code**, then download the `.nc` file.

## Features

- Checks the plan before generating: tools missing from the magazine, unsupported tool directions, missing speeds/feeds or toolpaths
- Configurable tool change format, program end code (M30/M2) and safe height
- Tool changes and spindle speed changes only when needed
- Summary of operations, tool changes, feed moves and the X/Y/Z range used
- Warning when the program goes below the bottom of the stock

## Open assumptions (to be confirmed)

1. Machine X = part x, machine Y = -(part z), machine Z = part y minus the top of the raw stock.
2. G54 is at the stock corner (x = 0, z = 0) on the top face of the raw stock.
3. T number = position in the machine magazine list.
4. Cutting and linking moves run at the planned feed rate.

## Limitations

- Only tool direction +Y (3-axis)
- Linear moves only (G0/G1), no arcs
- No coolant or tool length offset codes
- Output is **not verified**: always check it in a simulator such as CAMotics before running on a machine

## Repository layout

| Path | Contents |
|---|---|
| `app.py`, `gcode_engine.py`, `plan_reader.py` | The generator |
| `gami_logo.png`, `.streamlit/` | Logo and theme |
| `Example_V1/inputs/V1_Part_STEP.stp` | The example part |
| `Example_V1/step_b/` | Tool paths (`step_b.json`) and selected stock (`stock_selection.json`) |
| `Example_V1/step_d/production_plan.json` | Production plan: operations, tools, machines |
| `Example_V1/README.md` | Description of the V1 example |
