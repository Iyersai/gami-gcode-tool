from gscrib import GCodeBuilder # this imports the G code writer 'GCodeBuilder'(the main tool)
#GcodeBuilder is a class(a blueprint)written by gscrib that describes the Gcode writer
# 1. Setup the builder. 
# print_lines=True will show the G-code in the terminal as it's generated.
g = GCodeBuilder(output='gscrib_multi_drill.nc', print_lines=True)  # Creating a specific object 'g', and tells the object to create with the file name

# 2. Add Preamble (Machine Setup)
# g.write("G17 G90")
# g.raw("G21")
# g.raw("G54")

# # 3. Tool Change (Switching to the Drill)
# g.raw("M6 T2")      
# g.raw("M3 S10000") 
setup_commands = [
    "G17 G90",
    "G21",
    "G54",
    "M6 T2",
    "M3 S10000"
]

# Loop through the list and write each one
for command in setup_commands:
    g.write(command) 

# 4. The Holes (Data)
holes = [
    (10.0, 10.0),
    (40.0, 10.0),
    (40.0, 40.0),
    (10.0, 40.0)
]

# 5. The Loop (Notice how clean the movement commands are!)
for x, y in holes:
    g.rapid(z=5.0)             # The library writes "G0 Z5.000"
    g.rapid(x=x, y=y)          # The library writes "G0 X10.000 Y10.000"
    g.rapid(z=3.0)             # The library writes "G0 Z3.000"
    g.move(z=-10.0, F=250.0)   # The library writes "G1 Z-10.000 F250.000"
    g.rapid(z=5.0)             # The library writes "G0 Z5.000"

# 6. Postamble (Machine Shutdown)
g.write("M5")
g.write("M2")

# 7. Save and close the file
g.teardown()
print(g)

print("\nSuccess! File 'gscrib_multi_drill.nc' created.")