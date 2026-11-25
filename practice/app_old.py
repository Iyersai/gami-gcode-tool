import streamlit as st #Importing the web framework (the web page library) (st header "adds medium sized header")
import json # to read the JSON file
from gscrib import GCodeBuilder # the G -code writer

# 1. Page Setup
st.set_page_config(page_title="GAMI G-Code Tool", page_icon="#G(AMI)CODE", layout="wide") # configuaration of the browser tab
st.title("G(AMI)CODE GAMI Automated G-Code Generator")
st.markdown("Upload a JSON Work Plan to automatically generate machine-ready G-code.")
# Displays normal text: in the markdown format
# 2. Layout columns
col1, col2 = st.columns(2) # creating the columns (splitting the page into left and right)

with col1:
    st.header("1. Input Work Plan")
    # File Uploader
    uploaded_file = st.file_uploader("Upload your Work Plan (JSON)", type=["json"])
    
    
    if uploaded_file is not None:
        plan = json.load(uploaded_file)
        st.success("Work Plan loaded successfully!")
        with st.expander("View Uploaded Data"):
            st.json(plan)

with col2:
    st.header("2. Generated Output")
    if uploaded_file is not None:
        if st.button("Generate G-Code", type="primary"):
            # The Engine
            g = GCodeBuilder(output='web_output.nc', print_lines=False)
            
            g.write("G17 G90")
            g.write("G21")
            g.write("G54")
            
            for op in plan['operations']:
                g.write(f"(Begin operation: {op['name']})")
                g.write(f"M6 T{op['tool']}")        
                g.write(f"M3 S{op['speed']}")       

                if op['type'] == 'drill':
                    for hole in op['holes']:
                        g.rapid(z=5.0)
                        g.rapid(x=hole['x'], y=hole['y'])
                        g.rapid(z=3.0)
                        g.move(z=-10.0, F=op['feed'])
                        g.rapid(z=5.0)
                        
                elif op['type'] == 'profile':
                    first_point = op['path'][0]
                    g.rapid(z=5.0)
                    g.rapid(x=first_point['x'], y=first_point['y'])
                    g.rapid(z=-2.0) 
                    
                    for point in op['path'][1:]:
                        g.move(x=point['x'], y=point['y'], F=op['feed'])
                    g.rapid(z=5.0)
                    
            g.write("M5")
            g.write("M2")
            g.teardown()
            
            st.success("G-Code Generated Successfully!")
            
            # Read and display the output
            with open('web_output.nc', 'r') as file:
                gcode_text = file.read()
                
            st.text_area("G-Code Preview", gcode_text, height=400)
            
            # Download Button
            st.download_button(
                label="⬇️ Download G-Code File (.nc)",
                data=gcode_text,
                file_name="gami_generated.nc",
                mime="text/plain"
            )