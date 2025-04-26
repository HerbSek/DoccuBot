import os 
import requests
import fitz
import streamlit as st
import random
import time
import numpy as np 
import pandas as pd 
from groq import Groq 
from dotenv import load_dotenv
load_dotenv()

groq_key = os.getenv("groq-key")

client = Groq(api_key = groq_key)

st.set_page_config(page_title="DoccuBot", page_icon=":page_facing_up:", layout="wide")



with open('styles.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html = True)


custom_col_style = """
    <style>
    .col-box {
        margin-top: -20px; 
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }
    .col1-bg {
       background-color: #ff7f0e;  /* Orange background */
        background-color: #ffa64d;
        margin-bottom: 40px;
    }
    .col2-bg {
        background-color: #2ca02c;  /* Green background */
        background-color: #66cc66;
         margin-bottom: 40px;
    }
    .col3-bg {
       
          background-color: #1f77b4;  /* Blue background */
          background-color: #5ab7e8;
         margin-bottom: 40px;
    }
    .stApp {
        margin-top: -10px;
    }
    </style>
"""


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages = []


def function_AIResponse(prompt, file):
    greetings = ["hello", "hi", "hey", "good morning", "good evening", "what's up"]
    
    if prompt.lower().strip() in greetings:
        return "👋 Hi there! I'm DoccuBot. I can help you understand your PDF file. Would you like a summary, or do you have a question in mind?"

    file_content = file.read()
    if not file_content:
        return "Error: Uploaded file is empty."

    text = ''
    with fitz.open(stream=file_content, filetype="pdf") as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text += page.get_text("text")

    text = text[:6000]  # limit to avoid too much input
    content = f"""
    You are a helpful assistant reading a PDF. Analyze it and answer the user's question based on this content:
    {text}
    
    Question from user: {prompt}
    
    Be conversational, step-by-step, and helpful. Ask follow-up questions if needed.
    
    Use markdown formatting like:
    - Headings (`###`)
    - Bullet points (`-`)
    - Numbered steps
    - Code blocks (```python)
    - Quotes (`>`) if needed
    """
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": content}],
        model="llama-3.3-70b-versatile",
    )
    
    response = chat_completion.choices[0].message.content
    return response or "Hmm, something went wrong. Please try again later."



def response_generator(prompt, file):
    if file is None:
        yield "Please upload a file. Please check the sidebar to upload one!!!"
    else:
        # Write a function to work with Openai to retrive the response from the prompt and replace it with the string just below
        response = function_AIResponse(prompt, file)
        # for word in response.split('\n'):
        #     yield word + " "
        #     time.sleep(0.3)
        yield response   


write_up = "DoccuBot"
st.header(write_up, divider='rainbow')


st.markdown(custom_col_style, unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="col-box col1-bg">
        <p>DoccuBot: A state-of-the-art interactive platform for advanced document querying. Engage in intelligent conversations with your PDF files.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="col-box col2-bg">
        <p>Upload Documents: Seamlessly upload your PDF documents via the navigation sidebar. Our system processes files in real-time, providing rapid access to in-depth document insights.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="col-box col3-bg">
        <p>Query and Retrieve: Ask any technical or non-technical question regarding the content of your PDFs.</p>
    </div>
    """, unsafe_allow_html=True)



with st.sidebar:
    mylabel = st.header('Upload')
    file = st.file_uploader(' ', accept_multiple_files=False, type='pdf')  # Changed to singular `file`

    if file:        
        file_name = file.name
       
        files_s = pd.Series([file_name], name='PDFS')
        
        # st.write(files_s) // For some purposes

        # st.write(file)
        st.success('File uploaded successfully !!!')
    else:
        st.error("No file uploaded yet.")




for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



prompt = st.chat_input("Need help with your pdf?")


if prompt :     

    with st.chat_message("user"):
        st.markdown(prompt)
    

    st.session_state.messages.append({"role": "user", "content": prompt})
    if file:
     
        response = ""
        
        assistant_message = st.empty()

        for part in response_generator(prompt, file): 
            response += part  
            
           
            assistant_message.markdown(response)

      
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        
        response = "Please upload a PDF file in the sidebar to get started."
        
       
        with st.chat_message("assistant"):
            st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
