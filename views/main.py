import streamlit as st
from streamlit_option_menu import option_menu
from huggingface_hub import InferenceClient
from io import BytesIO
from PIL import Image
import os

hf_token=os.getenv("HF_TOKEN")

@st.cache_resource
def load_model():
    text2img_client = InferenceClient("stabilityai/stable-diffusion-3.5-large", token="hf_token")
    img2img_client = InferenceClient("stabilityai/stable-diffusion-xl-refiner-1.0", token="hf_token")
    return text2img_client,img2img_client

text2img_client,img2img_client=load_model()

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

if option == "Generate with Prompt":
    # Prompt Input
    prompt = st.text_input("Enter your prompt")

    # Generate Button in Center
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")
    with col2:
        generate_button = st.button("✨ Generate", use_container_width=True, type='primary')

    # Generate Image Logic
    if generate_button:
        if prompt:
            with st.spinner("Generating image..."):
                try:
                    # Add style to the prompt if not default
                    if style != "Default":
                        prompt += f" in {style} style."

                    # Generate Image
                    image = text2img_client.image_to_image(prompt)
                    if image:
                        # Display the Image
                        st.image(image, caption="Generated Image", use_container_width=True)

                        # Prepare the image for download
                        image_bytes = BytesIO()
                        image.save(image_bytes, format="PNG")
                        image_bytes.seek(0)
                        # Add a download button
                        st.download_button(
                            label="Download Image",
                            data=image_bytes,
                            file_name="sketchgen_generated_image.png",
                            mime="image/png",
                            help="Click to download the generated image."
                        )
                except Exception as e:
                    st.error(f"An error occurred while generating the image: {e}")
        else:
            st.error("Please enter a prompt!")


else:
    prompt=st.text_input("Enter your prompt  (Optional)")
    uploaded_image = st.file_uploader("Upload an Image", type=["jpeg", "jpg", "png"])

    if uploaded_image:
        st.sidebar.image(uploaded_image, caption="Uploaded Image")

    col1, col2, col3 = st.columns([1, 1, 1],gap="large")
    with col2: 
        generate_button=st.button("Generate",icon="✨",use_container_width=True,type='primary')

    if prompt:
        if style!="Default":
            prompt=prompt+f" in {style} style."
    else:
        prompt="Default prompt"

if generate_button:
    if uploaded_image:
        pil_image = Image.open(uploaded_image).convert("RGB")
        img_byte_arr = BytesIO()
        pil_image.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)
        with st.spinner("Generating image..."):
            generated_image = img2img_client.image_to_image(
                image=img_byte_arr,
                prompt="Transform this sketch into real image",
                strength=0.8,
                guidance_scale=7.5,
            )

            if generated_image:
                st.image(generated_image, caption="Generated Image")
            else:
                st.error("Image generation failed.")
    else:
        st.error("Please upload an image.")