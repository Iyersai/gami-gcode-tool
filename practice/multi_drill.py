# 1. Create the list to hold our G-code lines
gcode_lines = []

# 2. The Preamble (Machine Setup)
gcode_lines.append("(Begin preamble)")
gcode_lines.append("G17 G90")
gcode_lines.append("G21")
gcode_lines.append("G54")

# 3. Tool Change (Switching to the Drill)
gcode_lines.append("(Begin operation: TC: 5mm Drill)")
gcode_lines.append("M6 T2")      
gcode_lines.append("M3 S10000")  

# 4. The Drilling Movements (AUTOMATED!)
gcode_lines.append("(Begin Drilling)")

# Here is our list of holes. Each hole is an (X, Y) coordinate.
holes = [
    (10.0, 10.0),
    (40.0, 10.0),
    (40.0, 40.0),
    (10.0, 40.0)
]

# The 'for' loop goes through each hole in the list one by one.
for x, y in holes:
    gcode_lines.append("G0 Z5.000")                  # Lift to safe height : with f, you are telling python that look inside the {}, but dont just print it (if used print()). Here x.append() is used, so, 
    gcode_lines.append(f"G0 X{x:.3f} Y{y:.3f}")       # Move to the next hole : it sees the f, It sees {x:.3f}. It takes the value 10.0, converts it to a float with 3 decimal places: 10.000.; "G0 X10.000 Y40.000"
    gcode_lines.append("G0 Z3.000")                  # Move to reference height
    gcode_lines.append("G1 Z-10.000 F250.00")        # Drill down
    gcode_lines.append("G0 Z5.000")                  # Retract # technically, you dont need to add f, in the sentence, where there is no {} which means no variables here

# 5. The Postamble (Machine Shutdown)
gcode_lines.append("(Begin postamble)")
gcode_lines.append("M5")         
gcode_lines.append("M2")         

# 6. Print it to the screen (Optional debugging)
print("--- Generating G-Code for 4 Holes ---")
for line in gcode_lines:
    print(line)

# 7. Save it to a text file
import os # Operating system library that lets your code to talk with the computer file system
file_path = os.path.join(os.getcwd(), "multi_drill.nc") # os.getcwd - is to get the working directory, and asks pyton, where am I now? os.path.join(), takes the folder path and the file name to join them together
with open(file_path, "w") as file: # open(), tells the computer to open the file, file_path is the address that was created in the step 2, w is the write mode (if the computer already has the file somewhere, then erase it and start fresh)
    # 
    for line in gcode_lines:
        file.write(line + "\n")

print(f"\nSuccess! File created at: {file_path}")
print(gcode_lines)
print("generating")