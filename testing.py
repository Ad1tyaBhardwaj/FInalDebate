import os
import gtts
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from st_chat_message import message
load_dotenv('.env', override=True)


from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=1,
    openai_api_key='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'
)

difficulty = input("Enter difficulty (1-10): ")
topic = input("Enter the debate topic: ")
size = input("Enter size of debate --Type 0 for infinite debate: ")
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


while True:
    content = input('Your Turn: ')
    if content in ['quit','exit','bye']:
        print('Goodbye!')
        break

    response = chain.run({'content': content})
    improved_response = "Suggested Response: " + chain.run({'content': f"Please improve on: {content}"})
    print(response)
    print(improved_response)
    text= response
    sound = gtts.gTTS(text,lang="en")
    sound.save("Response.mp3")
    print('-'*50)



def main():

    st.set_page_config(page_title="DebateMaster",page_icon="😎")

    st.header("Debate for better world")

    act_difficulty = st.slider('Difficulty', 0, 23, 17)

    message("Hello world!", is_user=True)
    message("Hi")

    

