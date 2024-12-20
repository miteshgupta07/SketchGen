# Importing required libraries for Streamlit app, image generation, and file handling
import streamlit as st
from streamlit_option_menu import option_menu
from huggingface_hub import InferenceClient
from io import BytesIO
from PIL import Image
import os

# Setting up Hugging Face token from environment variable for secure access
hf_token = os.getenv("HF_TOKEN")

# Function to load the Stable Diffusion model from Hugging Face using the token


@st.cache_resource
def load_model():
    text2img_client = InferenceClient(
        "stabilityai/stable-diffusion-3.5-large", token=hf_token)
    return text2img_client


# Loading the model once during the app initialization
text2img_client = load_model()

# Title
st.markdown("<h1 align='center'>SketchGen 🎨</h1><h4 align='center' style='font-weight: normal;'>Transform your imagination into images from text or sketches</h4>", unsafe_allow_html=True)

# Sidebar configuration: Allow users to customize image style, resolution, and parameters
with st.sidebar:
    with st.expander("**Image Customization**", icon="🖌️", expanded=True):

        # Option to select the style of the generated image
        style = st.radio(label="Select Style", options=["Default", "Photorealistic", "Anime"], index=0, horizontal=True,
                         help="Choose the style of the image. 'Photorealistic' gives a more lifelike look, 'Anime' adds a stylized animated appearance.")

        # Option to select the resolution for the generated image
        image_resolution = st.radio("Image Resolution", options=["512x512", "768x768", "1024x1024"], index=0, horizontal=True,
                                    help="Select the resolution of the image. Higher resolutions offer more details but take longer to generate.")
        # Extract width and height for image resolution
        width, height = map(int, image_resolution.split('x'))

    with st.expander("**Parameter Customization**", icon="🛠️"):

        # Slider for adjusting inference steps (impact on image detail and generation time)
        inference_steps = st.slider("**Inference Steps**", min_value=10, max_value=100, value=50, step=1,
                                    help="Adjust the number of steps for generating the image. Higher values result in more detailed images but take longer to generate.")

        # Slider for adjusting the guidance scale (controls how closely the model follows the prompt)
        guidance_scale = st.slider("**Guidance Scale**", min_value=5.0, max_value=20.0, value=7.5, step=0.5,
                                   help="Control how closely the generated image aligns with your prompt. Higher values make the image more faithful to the prompt.")


# Option menu to switch between "Generate with Prompt" and "Generate with Image"
option = option_menu(
    menu_title="",  # Title of the menu
    options=["Generate with Prompt", "Generate with Image"],  # List of options
    icons=["pencil", "image"],  # Icons for each option
    # Orientation of the menu (horizontal or vertical)
    orientation="horizontal",
    default_index=0,  # Default index of the selected option
    styles={  # Custom styling options
        "container": {"background-color": "#181818"},  # Container style
        "icon": {"color": "#fabb23", "font-size": "18px"},  # Icon style
        # Navigation link style
        "nav-link": {"font-size": "20px", "text-align": "center", "color": "white", "font-weight": "normal", "font-family": "calibri"},
        # Selected option style
        "nav-link-selected": {"background-color": "#2d96fc", "color": "white"},
    }
)
# Generate image using text prompt if "Generate with Prompt" is selected
if option == "Generate with Prompt":

    # Input field for the user to enter a text prompt
    prompt = st.text_area("Enter your prompt", key="prompt",
                          placeholder="A futuristic cityscape at sunset", height=70)

    # Layout for the button and image display
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")
    with col2:

        # Button to trigger the image generation process
        generate_button = st.button(
            "✨ Generate", use_container_width=True, type='primary')

    # Image generation logic when the button is clicked
    if generate_button:
        if prompt:
            _, col, _ = st.columns([1.5, 1, 1.5])
            with col:
                with st.spinner("Generating image..."):
                    try:
                        # Modify the prompt if the style is not 'Default'
                        if style != "Default":
                            prompt += f" in {style} style."

                        # Call the model's text_to_image function to generate the image
                        image = text2img_client.text_to_image(
                            prompt=prompt,
                            guidance_scale=guidance_scale,
                            num_inference_steps=inference_steps,
                            width=width,
                            height=height
                        )

                        if image:

                            # Save the generated image in session state for persistence across interactions
                            st.session_state["generated_image"] = image

                            # Convert the image to a byte stream for download
                            image_bytes = BytesIO()
                            image.save(image_bytes, format="PNG")
                            image_bytes.seek(0)
                            image_from_bytes = Image.open(image_bytes)
                            image_size = image_from_bytes.size  # Get the image size for the filename

                            with col3:

                                # Adjust style name if it is 'Default'
                                if style == "Default":
                                    style = ""

                                # Create a download button with the generated image and its resolution
                                st.download_button(
                                    label="Download Image",
                                    data=image_bytes,
                                    file_name=f"sketchgen_{style}_generated_image_{image_size[0]}x{image_size[1]}.png",
                                    mime="image/png",
                                    use_container_width=True
                                )

                    except Exception as e:
                        # Handle any errors that occur during image generation
                        st.error(
                            f"An error occurred while generating the image: {e}")
        else:
            # Prompt user to enter a valid prompt if none is provided
            st.error("Please enter a prompt!")

    # Display the generated image if it is stored in session state
    if "generated_image" in st.session_state:
        st.image(st.session_state["generated_image"],
                 caption="Generated Image", use_container_width=True)


else:
    st.warning("The 'Generate with Image' feature is under development and will be available shortly. We appreciate your patience. Stay tuned for updates!")

    # prompt=st.text_input("Enter your prompt (Optional)")
    # uploaded_image = st.file_uploader("Upload an Image", type=["jpeg", "jpg", "png"])

    # if uploaded_image:
    #     st.sidebar.image(uploaded_image, caption="Uploaded Image")

    # col1, col2, col3 = st.columns([1, 1, 1],gap="large")
    # with col2:
    #     generate_button=st.button("Generate",icon="✨",use_container_width=True,type='primary')

    # if prompt:
    #     if style!="Default":
    #         prompt=prompt+f" in {style} style."
    # else:
    #     prompt="Default prompt"

    # if generate_button:
    #     if uploaded_image:
    #         pil_image = Image.open(uploaded_image).convert("RGB")
    #         img_byte_arr = BytesIO()
    #         pil_image.save(img_byte_arr, format='JPEG')
    #         img_byte_arr.seek(0)
    #         with st.spinner("Generating image..."):
    #             generated_image = img2img_client.image_to_image(
    #                 image=img_byte_arr,
    #                 prompt="Transform this sketch into real image",
    #                 strength=0.8,
    #                 guidance_scale=7.5,
    #             )

    #             if generated_image:
    #                 st.image(generated_image, caption="Generated Image")
    #             else:
    #                 st.error("Image generation failed.")
    #     else:
    #         st.error("Please upload an image.")
