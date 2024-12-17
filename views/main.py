import streamlit as st
from streamlit_option_menu import option_menu
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
# import torch

# Initialize Stable Diffusion model
# @st.cache_resource
# def load_model():
#     model_id = "stabilityai/stable-diffusion-2-1-base"
#     scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
#     pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
#     return pipe

# pipe = load_model()

# Sidebar: Customization options
with st.sidebar:

    with st.expander("**Image Customization**", icon="🛠️"):
    
        # Style selection using st.radio
        style = st.radio(label="Select Style",options=["Default", "Photorealistic", "Anime"],
            index=0,
            horizontal=True,
            help="Choose the style for the generated image."
        )

        # Image resolution selection using st.radio
        image_resolution = st.radio(
            "Image Resolution",
            options=["512x512", "768x768", "1024x1024"],
            index=0,
            horizontal=True,
            help="Select the resolution of the generated image."
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

option=option_menu(menu_title="",options=["Generate with Prompt","Generate with Image"],
            icons=["camera","camera"],
            orientation="horizontal",
            default_index=0)
# Generate based on user selection
if option == "Generate with Prompt":
    prompt = st.text_input("Enter your prompt")
    if st.button("✨ Generate"):
        if prompt:
            with st.spinner("Generating image..."):
                st.write("Hello")
                # image = pipe(prompt, guidance_scale=guidance_scale, num_inference_steps=inference_steps).images[0]
                st.image(image, caption="Generated Image")
                st.download_button("Download Image", image.to_bytes(), file_name="generated_image.png", mime="image/png")
        else:
            st.error("Please enter a prompt!")
else:
    uploaded_image = st.file_uploader("Upload an Image", type=["jpeg", "jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image")
    if st.button("✨ Generate"):
        with st.spinner("Generating image..."):
            # image = pipe(prompt=None, init_image=uploaded_image, guidance_scale=guidance_scale, num_inference_steps=inference_steps).images[0]
            # st.image(image, caption="Generated Image")
            # st.download_button("Download Image", image.to_bytes(), file_name="generated_image.png", mime="image/png")
            st.write("Hello")