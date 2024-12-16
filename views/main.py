import streamlit as st

st.title("SketchGen")
st.write("Description")

prompt=st.text_input("Enter your prompt")

st.radio("Select Style",options=["Default","Photorealistic","Anime"],horizontal=True)

image=st.file_uploader("Upload an Image",type=['jpeg','jpg','png'])
if image:
    st.image(image)