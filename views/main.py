import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:

        # Style selection using st.radio
    style = st.radio(
        "Select Style",
        options=["Default", "Photorealistic", "Anime"],
        index=0,
        help="Choose the style for the generated image."
    )
    
    with st.expander("**Parameter Customization**", icon="🛠️"):
        # Inference Steps
        inference_steps = st.slider(
            "**Inference Steps**",
            min_value=10, 
            max_value=100, 
            value=50, 
            step=1,
            help="Controls the number of steps for generating the image. Higher values produce more detailed results but takes more time."
        )
        
        # Guidance Scale
        guidance_scale = st.slider(
            "**Guidance Scale**",
            min_value=5.0, 
            max_value=20.0, 
            value=7.5, 
            step=0.5,
            help="Controls how strongly the model follows the prompt. Higher values produce images closer to the prompt.Lower values enables Creative Freedom."
        )
         # Image resolution selection using st.radio
        image_resolution = st.radio(
            "Image Resolution",
            options=["512x512", "768x768", "1024x1024"],
            index=0,
            help="Select the resolution of the generated image."
        )

option=option_menu(menu_title="",options=["Generate with Prompt","Generate with Image"],
            icons=["camera","camera"],
            orientation="horizontal",
            default_index=0)

if option=="Generate with Prompt":
    prompt=st.text_input("Enter your prompt")
else:
    st.file_uploader("Upload an Image",type=["jpeg","jpg","png"])

st.button("✨Generate")