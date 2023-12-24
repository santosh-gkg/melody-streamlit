import streamlit as st
from gradio_client import Client
import time


with st.sidebar:
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
image = "mld.png"

# Displaying image and title with adjusted column width
col1, col2 = st.columns([1, 3])  # Adjust the width ratios as needed

with col1:
    st.image(image, width=190)  # Adjust the width as needed

with col2:
    st.title("Your Emotions")
def main():
    if st.button("Generate Audio using GPT-3"):
        song_name = st.text_input("Enter your prompt here:")
        result = generate_audio(song_name)
        st.audio(result, format="audio/wav", start_time=0)
    if st.button("use your own lyrics"):
        song_name = st.text_input("Enter your prompt here:")
        result = generate_audio(song_name)
        st.audio(result, format="audio/wav", start_time=0)

def generate_audio(prompt):
    client = Client("https://suno-bark.hf.space/")
    
    # Show loading spinner
    result = client.predict(prompt, "Unconditional", fn_index=3)
    
    
    return result
if __name__ == "__main__":
    main()

    

