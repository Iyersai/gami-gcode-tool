import json
from gscrib import GCodeBuilder

# 1. Read the Work Plan
with open('work_plan_2.json', 'r') as file:
    plan = json.load(file)

# 2. Setup the builder
g = GCodeBuilder(output='auto_generated_2.nc', print_lines=True)

# 3. Preamble
g.write("G17 G90")
g.write("G21")
g.write("G54")

# 4. Loop through the OPERATIONS in the JSON
for op in plan['operations']:
    
    # --- Common Setup for every operation ---
    g.write(f"(Begin operation: {op['name']})")
    g.write(f"M6 T{op['tool']}")        # Tool Change
    g.write(f"M3 S{op['speed']}")       # Spindle On
    
    # --- Drill Logic ---
    if op['type'] == 'drill':
        for hole in op['holes']:
            g.rapid(z=5.0)
            g.rapid(x=hole['x'], y=hole['y'])
            g.rapid(z=3.0)
            g.move(z=-10.0, F=op['feed'])
            g.rapid(z=5.0)
            
    # --- Profile Logic ---
    elif op['type'] == 'profile':
        # Move to the start of the path
        first_point = op['path'][0]
        g.rapid(z=5.0)
        g.rapid(x=first_point['x'], y=first_point['y'])
        g.rapid(z=-2.0) # Plunge to cutting depth
        
        # Loop through the rest of the points to cut the shape
        for point in op['path'][1:]:
            g.move(x=point['x'], y=point['y'], F=op['feed'])
            
        g.rapid(z=5.0) # Retract

# 5. Shutdown
g.write("M5")
g.write("M2")
g.teardown()

print("Success! File 'auto_generated_2.nc' created from multiple operations.")