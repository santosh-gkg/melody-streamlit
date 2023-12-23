import streamlit as st
from gradio_client import Client
import time



def main():
    
    song_name = st.text_input("Enter your prompt here:")
    
    if st.button("Generate Audio"):
        result = generate_audio(song_name)
        st.audio(result, format="audio/wav", start_time=0)

def generate_audio(prompt):
    client = Client("https://suno-bark.hf.space/")
    
    # Show loading spinner
    result = client.predict(prompt, "Unconditional", fn_index=3)
    
    
    return result
if __name__ == "__main__":
    main()

    

