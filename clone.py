import streamlit as st
import openai

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets

import streamlit as st

with st.sidebar:
    st.header('_Configure_ the :blue[Model] :sunglasses:',divider='rainbow')
    st.write('\n')
    st.write('\n')

    title = st.text_input('Topic for Debate')
    if st.button('Confirm'):
        topic_global = title
        st.write('The current topic is', topic_global)

    st.divider()

    difficulty = st.slider('Select Difficulty', 0, 10, 5)
    if st.button('Change'):
        difficulty_global = difficulty
        st.write('difficulty has changed to ',difficulty_global)
    
    st.divider()
        
    with st.spinner("Loading..."):
        time.sleep(3)
    st.success("Done!")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""