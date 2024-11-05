<<<<<<< HEAD
import os 
import requests
import fitz
=======
>>>>>>> 12df44253ebbda89ead07a4fa6652b545a6a9ebf
import streamlit as st
import random
import time
import numpy as np 
import pandas as pd 
<<<<<<< HEAD
from dotenv import load_dotenv
st.set_page_config(page_title="DoccuBot", page_icon=":page_facing_up:", layout="wide")


load_dotenv()

with open('styles.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html = True)


=======
st.set_page_config(page_title="DoccuBot", page_icon=":page_facing_up:", layout="wide")










# custom_header = """
#     <style>
#     .custom-header {
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         background-color: white;
#         padding: 10px;
#         padding-top: 17px;
#         color: grey;
#         text-align: center;
#         font-size: 24px;
#         z-index: 1000;
#         # box-shadow: 0 4px 2px -2px gray;
#     }
#     # .custom-header a {
#     #     margin-left: 20px;
#     #     text-decoration: none;
#     #     color: white;
#     #     font-size: 18px;
#     #     padding: 5px 10px;
#     #     border-radius: 5px;
#     #     background-color: #f44336;
#     # }
#     .custom-header a:hover {
#         background-color: #e74c3c;
#     }
#     .stApp {
#         margin-top: 60px;
#     }
#     </style>
# """

# Inject the custom header
# st.markdown(custom_header, unsafe_allow_html=True)

# HTML for the custom header
# st.markdown("""
#     <div class="custom-header">
#         DoccuBot 
#     </div>
#     """, unsafe_allow_html=True)

>>>>>>> 12df44253ebbda89ead07a4fa6652b545a6a9ebf
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


<<<<<<< HEAD
# Function to work with the reponse 
def function_AIResponse(prompt, file):
    file_content = file.read()
    if not file_content:
        return "Error: Uploaded file is empty."
    text = ''
    with fitz.open(stream=file_content, filetype="pdf") as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text = page.get_text("text")
            text += text 
    url = "https://infinite-gpt.p.rapidapi.com/infinite-gpt"

    payload = {
        "query": prompt,
        "sysMsg": f'You are a friendly Chatbot that analyses PDFs and documents I upload strictly. I would give you the content from the pdf in here: {text}. I would ask any question from the pdf which i should get answers from that. if nothing is given, ask for a pdf content'
    }
    headers = {
        "x-rapidapi-key":  os.getenv('x-rapidapi-key'),
        "x-rapidapi-host": "infinite-gpt.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response1 = requests.post(url, json=payload, headers=headers)
    response = response1.json().get('msg')
     
    
    if response1.json()['message'] == 'You have exceeded the DAILY quota for Requests on your current plan, BASIC. Upgrade your plan at https://rapidapi.com/sujoyk211/api/infinite-gpt':
        return 'Daily Limit reached !!! Try again tomorrow :)'

        
    return(response)




def response_generator(prompt, file):
    if file is None:
        yield "Please upload a file. Please check the sidebar to upload one!!!"
    else:
        # Write a function to work with Openai to retrive the response from the prompt and replace it with the string just below
        response = function_AIResponse(prompt, file)
        for word in response.split('\n'):
            yield word + " "
            time.sleep(0.3)  

=======

def response_generator(prompt, file):
    if file is None:
        response = st.error(" Please upload a file. Please check the sidebar to upload one!!!")   
       
      
    if file is not None:
        response = "Lets start working!!"
        for word in response.split():
            yield word + " "
            time.sleep(0.2)
>>>>>>> 12df44253ebbda89ead07a4fa6652b545a6a9ebf

write_up = "DoccuBot"
st.header(write_up, divider='rainbow')


st.markdown(custom_col_style, unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

<<<<<<< HEAD
=======
# with col1:
#     st.write('An interactive tool used to chat with your pdf documents')
# with col2:
#     st.write('Upload your pdfs in the navigation bar ')
# with col3:
#     st.write('Ask it any question from the pdf to give out results')


>>>>>>> 12df44253ebbda89ead07a4fa6652b545a6a9ebf
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






<<<<<<< HEAD

=======
>>>>>>> 12df44253ebbda89ead07a4fa6652b545a6a9ebf
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

<<<<<<< HEAD

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
=======
prompt = st.chat_input("Need help with your pdf?")

if prompt:    
   
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt, file))    
    st.session_state.messages.append({"role": "assistant", "content": response})



# Parameters to use for the model (file: pdf , prompt: question, response: answer)

  

    

    

>>>>>>> 12df44253ebbda89ead07a4fa6652b545a6a9ebf
