import streamlit as st

# Setting the title for the page
st.title("Documentation 📃")

# Overview Section
st.header("📝 Overview")
st.write("""
This chatbot is designed to assist users by answering their queries in a conversational format.
The project is built using the following technologies:
- **Streamlit**: For creating an interactive web interface.
- **ChatGroq**: A robust conversational AI backend.
- **Python**: Core programming language for logic and integration.
- **Multilingual Support**: Enables interactions in multiple languages for a global user base. 🌍
""")

# How to Use the Chatbot Section
st.header("🤖 How to Use the Chatbot")
st.write("""
To use the chatbot:
1. Select the model type and customize parameters from the sidebar.
2. Choose your preferred language from the sidebar's **Language Options**. 🌐
3. Enter your query in the chat input box and get instant responses in the selected language.
4. View your conversation history directly in the chat interface.
""")
st.markdown("**Example Queries:**")
st.write("- `Who is Elon Musk ?` 🚀 (English)")
st.write("- `Persistent chat history ke baare mein samjhaaiye.` 📚 (Hindi)")

# Features Section
st.header("✨ Features")
st.write("""
The chatbot provides the following features:
- **Persistent Conversation History**: Maintains the flow of conversation. 🗣️
- **Customizable Models**: Adjust parameters like temperature and max tokens. ⚙️
- **Multilingual Support**: Communicate in languages like English, Hindi, Spanish, French, and German. 🌐
""")

# FAQs Section
st.header("❓ FAQs")
st.markdown("""
**Q: How can I reset the conversation history?**  
A: Simply refresh the page to start a new session with an empty chat history. 🔄

**Q: Can the chatbot answer queries in multiple languages?**  
A: Yes, you can select your preferred language from the sidebar and the chatbot will respond accordingly. 🌍
""")

# Acknowledgments Section
st.header("🙏 Acknowledgments")
st.write("""
This project was made possible with the following resources:
- **LangChain**: For managing chat history and prompts. 🔗
- **Groq Models**: High-performance conversational AI models. 🧠
""")

# Footer Section
st.write("For further details, please refer to the [project repository](https://github.com/miteshgupta07/QA-Chatbot) or contact me through the links provided on the '**About Me**' page. 📞")
