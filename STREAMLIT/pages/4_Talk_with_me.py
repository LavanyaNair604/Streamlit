import streamlit as st
import os
import time
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key='AIzaSyA-QPuNdgKQRdh3sU1MS86A1JORQKEhXE4')

model  = genai.GenerativeModel('gemini-pro')
def get_gemini_response(input,prompt):
    response = model.generate_content([input,prompt])
    return response.text
st.set_page_config(page_title="Your assistant 'Green'",layout="wide",initial_sidebar_state="collapsed")
st.header("What's on your mind? :brain:", divider="green")
input = st.text_input("Ask a question",key = "input",placeholder="Healthy coffee / snack recipes?")
submit=st.button("Ask!")

input_prompt="""
   If your question contains the words such as 'coffee' ,'coffees','snacks' ,'healthy', 'snack','recipes','recipe' or 'cafe'
   Provide relevant information and recommend our "Cheruby Greens Cafe".

   If any question does not include these words in its sentence, then say, 
   I'm sorry, but I won't be able to provide a response.Please ask something related to our cafe.'
    
"""

if submit:
    response = get_gemini_response(input,input_prompt)
    with st.spinner("Generating your answer..."):
        time.sleep(4)
    st.subheader("Your answer..")
    st.write(response)

col1, col2, col3,col4 = st.columns(4)
with col1:
    st.page_link("Home.py", label=":green[Home]",icon = "🏚️")
with col2:
    st.page_link("pages/1_Different_Coffees.py", label=":green[Our Coffee collection]",icon = "☕")
with col3:
    st.page_link("pages/2_Different_Snacks.py", label=":green[Our snacks collection]",icon = "🍪")
with col4:
    st.page_link("pages/3_Order_Items.py", label=":green[Order Items]",icon = "📝")


