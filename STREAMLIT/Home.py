import streamlit as st
# from langchain.llms import OpenAI
import time
st.set_page_config(page_title="Cheruby Greens Cafe",layout="wide",initial_sidebar_state="collapsed")
st.header("Cheruby Greens Cafe :coffee:", divider="green")
with st.spinner('Please Wait...'):
    time.sleep(1)
st.toast('Hi!')
time.sleep(.5)
st.toast('Im your assistant Green ',icon = '🤖')
time.sleep(.5)
st.toast('How do you brew?!')
col1, col2 = st.columns(2)
    

with col1:
    st.image("STREAMLIT\pages\CAFESS.jpg")
    
with col2:
    st.header(" Coffee and Snacks is a beautiful combination! :cookie:")
    st.write("Coffee is a beverage made from the roasted and ground seeds of the coffee plant. It is one of the most popular beverages in the world, along with water and tea.")
    st.write("""Try a **cappuccino**, **mocha**, or **latte** first
    Flavored coffee can help you get used to the taste of coffee with sugar, cream, and other flavors""")
    st.page_link("pages/1_Different_Coffees.py", label=":green[Explore coffee]",icon = "☕")
    st.page_link("pages/2_Different_Snacks.py", label=":green[Explore snacks]",icon = "🍩")
    st.page_link("pages/3_Order_Items.py", label=":green[Order]",icon = "📝")

#     openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# def generate_response(input_text):
#     llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#     st.info(llm(input_text))

# with st.form('my_form'):
#     text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
#     submitted = st.form_submit_button('Submit')
#     if not openai_api_key.startswith('sk-'):
#         st.warning('Please enter your OpenAI API key!', icon='⚠')
#     if submitted and openai_api_key.startswith('sk-'):
#         generate_response(text)
