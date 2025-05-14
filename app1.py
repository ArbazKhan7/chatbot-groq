from langchain_core.prompts import ChatPromptTemplate
from  langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_community.llms import  Ollama
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
#Prompt Template

prompts= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question: {question}")
    ]
)

#Streamlit

st.title("Langchain Demo with ChatGroq Api")
input_text=st.text_input("Search the topic u want")

#Local model

#llm = Ollama(model="llama2")
#Groq LLM API
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="Llama3-8b-8192"
)
output_parser=StrOutputParser()
chain =prompts | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
