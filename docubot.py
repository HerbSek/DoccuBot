import streamlit as st
import random
import time

st.set_page_config(page_title="Custom Streamlit App", page_icon=":smile:", layout="wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_streamlit_watermark = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { bottom: 0px; }
    .viewerBadge_link__1S137 { display: none !important; }
    </style>
    """
st.markdown(hide_streamlit_watermark, unsafe_allow_html=True)

def response_generator(prompt):
    response = "Lets start working!!"
    for word in response.split():
        yield word + " "
        time.sleep(0.1)

write_up = "Docu_Bot"
st.header(write_up, divider='rainbow')

col1,col2,col3 = st.columns(3)

with col1:
    st.write('An interactive tool used to chat with your pdf documents')
with col2:
    st.write('Upload your pdfs in the navigation bar ')
with col3:
    st.write('Ask it any question from the pdf to give out results')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Chat with Docu_Bot")
if prompt:    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    

        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


with st.sidebar:
    st.title('Docu_Bot')

