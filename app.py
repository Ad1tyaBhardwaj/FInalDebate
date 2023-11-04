from dotenv import find_dotenv, load_dotenv
#from transformers import pipeline
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain, OpenAI


load_dotenv(find_dotenv())

#llm
def generate_response(scenario):
    template = """
    you are a story teller;
    you can generate a short story based on a simple narrative, the story should be no more than 20 words

    CONTEXT: {scenario}
    STORY:
    """

    prompt: PromptTemplate(template = template, input_variable=["scenario"])

    story_llm = LLMChain(llm=OpenAI(
        model_name="gpt-3.5-turbo", temprature=1), prompt=prompt, verbose=True)
    
    story = story_llm.predict(scenario=scenario)

    print(story)
    return(story)


generate_response("2 people standing on a beach")