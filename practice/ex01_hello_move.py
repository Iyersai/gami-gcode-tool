"""Example 1: the smallest Gscrib program (from the official quick-start).
LEARN: create the builder, set the start position, rapid vs feed move, tool on/off, teardown.
CHECK: open ex01.nc. Which Python line made which G-code line?
TRY:   change the target to x=30, y=5 and the feed rate to 800."""
from gscrib import GCodeBuilder

g = GCodeBuilder(output="ex01.nc", print_lines=True)

g.set_axis(x=0, y=0, z=0)       # tell Gscrib where the tool is now
g.rapid(z=5)                    # fast move up (no cutting)
g.rapid(x=10, y=10)             # fast move to X10 Y10
g.tool_on("clockwise", 1000)    # spindle on, 1000 rpm
g.move(x=20, y=20, F=1500)      # cutting move at feed 1500
g.tool_off()                    # spindle off
g.teardown()                    # finish and save the file
