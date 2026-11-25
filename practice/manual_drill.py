# 1. We create a list to hold our G-code lines
gcode_lines = []

# 2. The Preamble (Machine Setup)
gcode_lines.append("(Begin preamble)")
gcode_lines.append("G17 G90")
gcode_lines.append("G21")
gcode_lines.append("G54")

# 3. Tool Change (Switching to the Drill)
gcode_lines.append("(Begin operation: TC: 5mm Drill)")
gcode_lines.append("M6 T2")      # T2 is the drill
gcode_lines.append("M3 S10000")  # Spindle on at 10,000 RPM

# 4. The Drilling Movement
gcode_lines.append("(Begin Drilling)")
gcode_lines.append("G0 Z5.000")            # Rapid move to safe Z height
gcode_lines.append("G0 X25.000 Y25.000")   # Rapid move to the hole center
gcode_lines.append("G0 Z3.000")            # Rapid move to reference height
gcode_lines.append("G1 Z-10.000 F250.00")  # Feed down to Z=-10
gcode_lines.append("G0 Z5.000")            # Retract back up

# 5. The Postamble (Machine Shutdown)
gcode_lines.append("(Begin postamble)")
gcode_lines.append("M5")         # Spindle off
# gcode_lines.append("M2")         # End of program


# 6. Print it to the screen so we can see it
# print("--- Generating G-Code ---")
# for line in gcode_lines:
#     print(line)
for line in gcode_lines:
    print(line)
    print("--- Next line ---")

# 7. Save it to a text file
import os # Operating system library that lets your code to talk with the computer file system
file_path = os.path.join(os.getcwd(), "my_drilling_test.nc") # os.getcwd - is to get the working directory, and asks pyton, where am I now? os.path.join(), takes the folder path and the file name to join them together
with open(file_path, "w") as file: # open(), tells the computer to open the file, file_path is the address that was created in the step 2, w is the write mode (if the computer already has the file somewhere, then erase it and start fresh)
    # 
    for line in gcode_lines:
        file.write(line + "\n")

print(f"\nSuccess! File created at: {file_path}")
print(gcode_lines)
