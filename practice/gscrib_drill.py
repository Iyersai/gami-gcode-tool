from gscrib import GCodeBuilder # this imports the G code writer 'GCodeBuilder'(the main tool)
#GcodeBuilder is a class(a blueprint)written by gscrib that describes the Gcode writer
# 1. Setup the builder. 
# print_lines=True will show the G-code in the terminal as it's generated.
g = GCodeBuilder(output='gscrib_multi_drill.nc', print_lines=True)  # Creating a specific object 'g', and tells the object to create with the file name
# print_lines=True : means “also show each line in the terminal while it’s being generated”. With False or without it, you’d only get the file. 
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
#g.write(cmd): This is a function inside gscrib. It takes whatever string you give it (like "G21") and writes it exactly as-is to the file. It adds a new line automatically.
#Why use it? It's used for commands that don't involve moving the tool to a specific X/Y/Z coordinate (like turning on the spindle or setting the coordinate system).
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
#Each time through the loop, python takes the next pair and puts the first number in x and the secound number in y. pass 1 has x 10, y 10, pass 2 has x 40, y 10, and so on.
# 5. The Loop (Notice how clean the movement commands are!)
for x, y in holes:
    g.rapid(z=5.0)             # The library writes "G0 Z5.000" # Fast move up to Z5, retracts to a safe height before moving sideways.
    g.rapid(x=x, y=y)          # The library writes "G0 X10.000 Y10.000" # it continues to the loop of the x and y coordinates specified in the upper loop (goes towards its center)
    g.rapid(z=3.0)             # The library writes "G0 Z3.000" # Moves down close towards the center
    g.move(z=-10.0, F=250.0)   # The library writes "G1 Z-10.000 F250.000" # drills
    g.rapid(z=5.0)             # The library writes "G0 Z5.000" # comes up

# 6. Postamble (Machine Shutdown)
g.write("M5")
g.write("M2")

# 7. Save and close the file
g.teardown() # tells the gcrib, that I am done, please close the file and save itto the hard drive
print(g)

print("\nSuccess! File 'gscrib_multi_drill.nc' created.")