import streamlit as st
from langchain.llms import OpenAI

st.title('🦉🔗 GeniTester will help you to create the test cases')

openai_api_key = st.sidebar.text_input('Type OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'Enter your use case here and I will give you detailed test cases based on your app only.')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠️')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
