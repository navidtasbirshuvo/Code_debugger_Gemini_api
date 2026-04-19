import streamlit as st
from api_calling import issue_generator,hints_generator,solution_generator
from PIL import Image 
import os

st.title("Code Debuger")
st.markdown("### Here is your code debuger")
st.divider()

with st.sidebar:
    st.header("Controls")
    images= st.file_uploader("upload your code",
    type=['jpg','png','jpeg'],
    accept_multiple_files=True)

    pillow_image=[Image.open(img) for img in images]

    if images:
        if len(images)>3:
            st.error("Please upload at most 3 images")
        
        else:
            cols= st.columns(len(images))
            for i, img in enumerate(images):
                with cols[i]:
                    st.image(img)
                
    select_option =st.selectbox( "Enter the Option",
    ('Hints','Solution with code'),
    index = None,
    placeholder="Select option"
    )
    
    pressed = st.button("Please click for debug",type="primary")
    if pressed:
        if not images:
            st.error("Please upload at least one image")
        elif not select_option:
            st.error("Please select the option")
    
if pressed and images and select_option:
    #issue 
    with st.container(border=True):
        st.subheader("Issue")
        with st.spinner("generating Issues"):
            generated_issue=issue_generator(pillow_image)
            st.markdown(generated_issue)

    #hints & solution
    with st.container(border=True):
        if select_option=="Hints":
            st.subheader("Hints")
            with st.spinner("Generating hints"):
                generated_hints=hints_generator(pillow_image)
                st.markdown(generated_hints)
        elif select_option=="Solution with code":
            st.subheader("Solution")
            with st.spinner("Generating solution"):
                generated_solution=solution_generator(pillow_image)
                st.markdown(generated_solution)




        


            
    