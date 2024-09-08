import streamlit as st
import random
import time

def response_generator(prompt):
    response = "Lets start working!!"
    for word in response.split():
        yield word + " "
        time.sleep(0.1)

write_up = "Docu_Bot"
st.header(write_up, divider='rainbow')

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

