import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ['OPENAI_API_KEY']=openai_key

# streamlit framework

st.title('langchain With OpenAI API')
input_text=st.text_input('search the you want')



# OPENAI LLMS
llm = OpenAI(temperature=0.3)

if input_text:
    st.write(llm(input_text))





