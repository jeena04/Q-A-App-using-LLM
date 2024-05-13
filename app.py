#Hello! It seems like you want to import the Streamlit library in Python. Streamlit is a powerful open-source framework used for building web applications with interactive data visualizations and machine learning models. To import Streamlit, you'll need to ensure that you have it installed in your Python environment.
#Once you have Streamlit installed, you can import it into your Python script using the import statement,

import streamlit as st

from dotenv import load_dotenv

load_dotenv()

#New import from langchain, which replaces the above
from langchain.llms import HuggingFaceHub

#When deployed on huggingface spaces, this values has to be passed using Variables & Secrets setting, as shown in the video :)
import os
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")

#llm_model=HuggingFaceHub(huggingfacehub_api_token=os.environ['HUGGINGFACE_API_KEY'],
                         #repo_id=model_id,
                         #model_kwargs={"temperature":0.5, 'max_new_tokens':250})
#Function to return the response
def load_answer(question):
    # "interneuronai/az-question-answering" model is depreciated, so using the latest one https://platform.openai.com/docs/deprecations
    llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['HUGGINGFACE_API_KEY'],
                         repo_id="mistralai/Mistral-7B-Instruct-v0.2",
                         model_kwargs={"temperature":0.5, 'max_new_tokens':250})

    #Last week langchain has recommended to use invoke function for the below please :)
    answer=llm.invoke(question)
    return answer


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = load_answer(user_input)

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)

