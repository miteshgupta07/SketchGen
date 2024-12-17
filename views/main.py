import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
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
        
option=option_menu(menu_title="",options=["Generate with Prompt","Generate with Image"],
            icons=["camera","camera","camera"],
            orientation="horizontal",
            default_index=0)

prompt=st.text_input("Enter your prompt")

style=option_menu(menu_title="Select Style",
            menu_icon="brilliance",
            options=["Default","Photorealistic","Anime"],
            icons=["camera","camera","camera"],
            orientation="horizontal",
            default_index=0)

image_resolution=option_menu(menu_title="Image Resolution",
            menu_icon="brilliance",
            options=["512x512","768x768","1024x1024"],
            icons=["camera","camera","camera"],
            orientation="horizontal",
            default_index=0)

st.button("✨Generate")

