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
def lyrics_generator(prompt, user_key):
    

    client = OpenAI(api_key=user_key)
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are song writer, skilled in writing romantic songs with creative flair under 30 words."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

with st.sidebar:
    st.title("How to use?")
    st.markdown("Enter your prompt in the text box below and click on the button to generate the audio.")
    st.markdown("<hr>", unsafe_allow_html=True)
    user_key = st.text_input("Enter your OpenAI API key here:")
    st.title("About")
    st.markdown("Melodify is a web app that converts your text into a song of your choice. It uses GPT-3 to generate the lyrics and HuggingFace's Bark Model to generate the audio.")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.title("Contributors")
    st.markdown("Aditya Sharma")
    st.markdown("Santosh Kumar")
    st.markdown("Dibas Kumar")
    st.markdown("Aditya Tiwari")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if user_key:
    if prompt := st.chat_input("what would you like to hear?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        prompt = lyrics_generator(prompt, user_key)
        prompt="♪"+prompt+"♪"
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        client = Client("https://suno-bark.hf.space/")
        result = client.predict(prompt, "Speaker 1 (en)", fn_index=3)
        greetings = "Enjoy your Melodified song!"
        message = st.chat_message("assistant")
        message.markdown(greetings)
        st.session_state.messages.append({"role": "assistant", "content": message})
        message.audio(result, format="audio/wav", start_time=0)
    
    
    
   

#available speakers
#['Unconditional', 'Announcer', 'Speaker 0 (en)', 'Speaker 1 (en)', 'Speaker 2 (en)', 'Speaker 3 (en)', 'Speaker 4 (en)', 'Speaker 5 (en)', 'Speaker 6 (en)', 'Speaker 7 (en)', 'Speaker 8 (en)', 'Speaker 9 (en)', 'Speaker 0 (de)', 'Speaker 1 (de)', 'Speaker 2 (de)', 'Speaker 3 (de)', 'Speaker 4 (de)', 'Speaker 5 (de)', 'Speaker 6 (de)', 'Speaker 7 (de)', 'Speaker 8 (de)', 'Speaker 9 (de)', 'Speaker 0 (es)', 'Speaker 1 (es)', 'Speaker 2 (es)', 'Speaker 3 (es)', 'Speaker 4 (es)', 'Speaker 5 (es)', 'Speaker 6 (es)', 'Speaker 7 (es)', 'Speaker 8 (es)', 'Speaker 9 (es)', 'Speaker 0 (fr)', 'Speaker 1 (fr)', 'Speaker 2 (fr)', 'Speaker 3 (fr)', 'Speaker 4 (fr)', 'Speaker 5 (fr)', 'Speaker 6 (fr)', 'Speaker 7 (fr)', 'Speaker 8 (fr)', 'Speaker 9 (fr)', 'Speaker 0 (hi)', 'Speaker 1 (hi)', 'Speaker 2 (hi)', 'Speaker 3 (hi)', 'Speaker 4 (hi)', 'Speaker 5 (hi)', 'Speaker 6 (hi)', 'Speaker 7 (hi)', 'Speaker 8 (hi)', 'Speaker 9 (hi)', 'Speaker 0 (it)', 'Speaker 1 (it)', 'Speaker 2 (it)', 'Speaker 3 (it)', 'Speaker 4 (it)', 'Speaker 5 (it)', 'Speaker 6 (it)', 'Speaker 7 (it)', 'Speaker 8 (it)', 'Speaker 9 (it)', 'Speaker 0 (ja)', 'Speaker 1 (ja)', 'Speaker 2 (ja)', 'Speaker 3 (ja)', 'Speaker 4 (ja)', 'Speaker 5 (ja)', 'Speaker 6 (ja)', 'Speaker 7 (ja)', 'Speaker 8 (ja)', 'Speaker 9 (ja)', 'Speaker 0 (ko)', 'Speaker 1 (ko)', 'Speaker 2 (ko)', 'Speaker 3 (ko)', 'Speaker 4 (ko)', 'Speaker 5 (ko)', 'Speaker 6 (ko)', 'Speaker 7 (ko)', 'Speaker 8 (ko)', 'Speaker 9 (ko)', 'Speaker 0 (pl)', 'Speaker 1 (pl)', 'Speaker 2 (pl)', 'Speaker 3 (pl)', 'Speaker 4 (pl)', 'Speaker 5 (pl)', 'Speaker 6 (pl)', 'Speaker 7 (pl)', 'Speaker 8 (pl)', 'Speaker 9 (pl)', 'Speaker 0 (pt)', 'Speaker 1 (pt)', 'Speaker 2 (pt)', 'Speaker 3 (pt)', 'Speaker 4 (pt)', 'Speaker 5 (pt)', 'Speaker 6 (pt)', 'Speaker 7 (pt)', 'Speaker 8 (pt)', 'Speaker 9 (pt)', 'Speaker 0 (ru)', 'Speaker 1 (ru)', 'Speaker 2 (ru)', 'Speaker 3 (ru)', 'Speaker 4 (ru)', 'Speaker 5 (ru)', 'Speaker 6 (ru)', 'Speaker 7 (ru)', 'Speaker 8 (ru)', 'Speaker 9 (ru)', 'Speaker 0 (tr)', 'Speaker 1 (tr)', 'Speaker 2 (tr)', 'Speaker 3 (tr)', 'Speaker 4 (tr)', 'Speaker 5 (tr)', 'Speaker 6 (tr)', 'Speaker 7 (tr)', 'Speaker 8 (tr)', 'Speaker 9 (tr)', 'Speaker 0 (zh)', 'Speaker 1 (zh)', 'Speaker 2 (zh)', 'Speaker 3 (zh)', 'Speaker 4 (zh)', 'Speaker 5 (zh)', 'Speaker 6 (zh)', 'Speaker 7 (zh)', 'Speaker 8 (zh)', 'Speaker 9 (zh)']
  
    # Add assistant response to chat history
    
    