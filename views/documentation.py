import streamlit as st

# Setting the title for the page
st.markdown("<h1 align='center'>Documentation 📃</h1>",unsafe_allow_html=True)

# Overview Section
st.header("📝 Overview")
st.write("""
**SketchGen** is an innovative tool designed to transform text prompts or sketches into visually stunning images.  
This project utilizes cutting-edge AI models to deliver accurate and customizable outputs.  
Key technologies used in this project:
- **Streamlit**: For creating an interactive web interface.
- **Stable Diffusion 3.5**: A state-of-the-art image generation model.
- **Python**: Core programming language for logic and integration.
""")

# How to Use SketchGen Section
st.header("💡How to Use SketchGen")
st.write("""
To generate an image:
1. Navigate to the **Generate with Prompt** tab.
2. Enter a text description of the image you want to generate.
3. Customize the **Style**, **Resolution**, and **Generation Parameters** in the sidebar:
   - Select your preferred **style** (Default, Photorealistic, Anime).
   - Choose an **image resolution** (512x512, 768x768, 1024x1024).
   - Adjust **Inference Steps** and **Guidance Scale** as needed.
4. Click the **Generate** button to create your image.  
5. Once the image is generated, you can download it directly to your device.
""")
st.markdown("**Example Prompts:**")
st.write("- `A futuristic cityscape at sunset` 🌇")
st.write("- `An anime-style character holding a magical sword` ✨")

# Features Section
st.header("✨ Features")
st.write("""
- **Prompt-Based Image Generation**: Create detailed images using descriptive text prompts. 📝
- **Style Customization**: Choose from Default, Photorealistic, and Anime styles. 🎨
- **Resolution Options**: Generate images at 512x512, 768x768, or 1024x1024 resolution. 📐
- **Parameter Adjustments**:
  - **Inference Steps**: Control the image generation process for greater detail. 🔧
  - **Guidance Scale**: Adjust the alignment of the image with the provided prompt. 🛠️
- **Download Capability**: Save your generated images with detailed filenames. 💾
""")

# FAQs Section
st.header("❓ FAQs")
st.markdown("""
**Q: How do I choose the best parameters for my image?**  
A: Experiment with **Inference Steps** (higher values for detail) and **Guidance Scale** (7.5 is recommended for most cases).  

**Q: Can I upload sketches to generate images?**  
A: The **Generate with Image** feature is under development and will be available soon.  

**Q: What styles are available for image generation?**  
A: You can select from Default, Photorealistic, and Anime styles in the sidebar.  

**Q: What resolutions are supported?**  
A: You can generate images in 512x512, 768x768, or 1024x1024 resolution. Choose your preference from the sidebar.
""")

# Acknowledgments Section
st.header("🙏 Acknowledgments")
st.write("""
This project was made possible with:
- **Hugging Face**: Providing the Stable Diffusion 3.5 model and inference APIs. 🤗
- **Streamlit**: Enabling seamless user interaction and customization. 🚀
""")

# Footer Section
st.write("For further details, please refer to the [project repository](https://github.com/miteshgupta07/SketchGen) or contact me through the **About Developer** page. 📞")
