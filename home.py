import streamlit as st
from langchain.prompts import PromptTemplate
from datetime import datetime

st.write("Hello World!")

a = [1, 2, 3, 4]
d = {"x": 1}


p = PromptTemplate.from_template("xxx")

PromptTemplate

p

a
d


st.selectbox("Choose your model", ("GPT-3", "GPT-4"))
