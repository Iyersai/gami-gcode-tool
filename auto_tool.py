import json
from gscrib import GCodeBuilder

# 1. Read the Work Plan file
with open('work_plan.json', 'r') as file: # this opens the json file in a readable format manner
    plan = json.load(file) # with open(...) as file:: This opens the work_plan.json file in 'r' (read) mode. The with statement ensures the file is automatically closed after we are done. 
    #json.load(file): This reads the text inside the JSON file and converts it into a Python dictionary named PLAN.
    #If your JSON had {"spindle_speed": 12000}, then plan becomes {"spindle_speed": 12000}. Now Python knows exactly what numbers to use.

# 2. Setup the G-code builder
g = GCodeBuilder(output='auto_generated.nc', print_lines=True)

# 3. Write the Preamble using data from the JSON
g.write("G17 G90")
g.write("G21")
g.write("G54")

# Use the tool number and spindle speed from the JSON
g.write(f"M6 T{plan['tool_number']}") # during this write function, the program, looks inside the PLAN dictionary, and takes the tool number as well as the spindle speed (f string properties)
g.write(f"M3 S{plan['spindle_speed']}")

# 4. Loop through the holes in the JSON
for hole in plan['holes']:
    x = hole['x']
    y = hole['y']
    
    g.rapid(z=5.0)
    g.rapid(x=x, y=y)
    g.rapid(z=3.0)
    # Use the feed rate from the JSON
    g.move(z=-10.0, F=plan['feed_rate']) # drills with the respective feed from the JSON file
    g.rapid(z=5.0)

# 5. Write the Postamble
g.write("M5")
g.write("M2")
g.teardown()

print("Success! File 'auto_generated.nc' created from the Work Plan.")