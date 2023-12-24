import streamlit as st
from gradio_client import Client
from openai import OpenAI, AuthenticationError

image = "mld.png"

# Displaying image and title with adjusted column width
col1, col2 = st.columns([1, 3])  # Adjust the width ratios as needed

with col1:
    st.image(image, width=190)  # Adjust the width as needed

with col2:
    st.title("Your Emotions")

# App title
# st.set_page_config(page_title="Melodify", page_icon="🎵", layout="centered", initial_sidebar_state="expanded")

# Hugging Face Credentials
with st.sidebar:
    st.title('Melodify')
    st.title("How to use?")
    st.markdown("Enter your prompt in the text box below and click on the button to generate the audio.")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.title("About")
    st.markdown("Melodify is a web app that converts your text into a song of your choice. It uses GPT-3 to generate the lyrics and HuggingFace's Bark Model to generate the audio.")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.title("Contributors")
    st.markdown("Aditya Sharma")
    st.markdown("Santosh Kumar")
    st.markdown("Dibas Kumar")
    st.markdown("Aditya Tiwari")
    # hf_email = st.text_input('Enter E-mail:', type='password')
    # hf_pass = st.text_input('Enter password:', type='password')
    # if not (hf_email and hf_pass):
    #     st.warning('Please enter your credentials!', icon='⚠️')
    # else:
    #     st.success('Proceed to entering your prompt message!', icon='👉')
    
    
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    st.text('Logging in to Hugging Face...')
   
    # Create ChatBot                        
    

# User-provided prompt
if prompt := st.chat_input("enter your prompt here"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("write your prompt here"):
        with st.spinner("Generating your song..."):
            
            prompt="♪"+prompt+"♪"
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            client = Client("https://suno-bark.hf.space/")
            result = client.predict(prompt, "Speaker 1 (en)", fn_index=3)
            greetings = "Enjoy your Melodified song!"
            
            message.markdown(greetings)
            st.session_state.messages.append({"role": "assistant", "content": message})
            message.audio(result, format="audio/wav", start_time=0)
    message = {"role": "assistant", "content": result}
    st.session_state.messages.append(message)