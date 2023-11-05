import streamlit as st
import openai
import time
import os
import gtts
from dotenv import load_dotenv, find_dotenv
import streamlit as st
import pyttsx3
load_dotenv('.env', override=True)
text_speech = pyttsx3.init()


from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate


def debate_bot_response(content, topic, difficulty):
    llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=1,
    openai_api_key='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')

    prompt = ChatPromptTemplate(
    input_variables=['content'],
    messages=[
        SystemMessage(content=f'You are a debating with the person on the topic: "{topic}". You need to counter the points given by user. Assuming it as a game, you need to counter the user based on the difficulty given. On a scale of 1-10, where 1 means Giving very low level of counters and letting the user win, and 10 means aggressivly countering every point of user, and trying to defeat the user. The current difficulty is: "{difficulty}". Give responses in not more than 40 words.'),
        HumanMessagePromptTemplate.from_template('{content}')
       ]
    )

    chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=False
    )
    if content in ['quit','exit','bye']:
        print('Goodbye!')
        return
    response = chain.run({'content': content})
    print(response)
    return response


debate_bot_response("I think AI will take away all jobs","future of AI",1)



difficulty_global = 10
topic_global = ""



#WEBSITE
st.title("Debate Master")

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

    with st.spinner("Thinking..."):
        response = debate_bot_response(prompt, topic_global, difficulty_global)
        responsee = f"{response}"
        with st.chat_message("assistant"):
            st.markdown(responsee)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": responsee})
