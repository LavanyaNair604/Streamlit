import streamlit as st
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
    st.image("STREAMLIT/pages/CAFESS.jpg")
    
with col2:
    st.header(" Coffee and Snacks is a beautiful combination! :cookie:")
    st.write("Coffee is a beverage made from the roasted and ground seeds of the coffee plant. It is one of the most popular beverages in the world, along with water and tea.")
    st.write("""Try a **cappuccino**, **mocha**, or **latte** first
Flavored coffee can help you get used to the taste of coffee with sugar, cream, and other flavors""")
    st.page_link("pages/1_Different_Coffees.py", label=":green[Explore coffee here]",icon = :coffee:)
    st.link_button("Yummy coffee", "https://github.com/LavanyaNair604/Streamlit/blob/main/STREAMLIT/pages/1_Different_Coffees.py",type="primary")
    st.link_button("Yum, Yum food", "STREAMLIT/pages/2_Different_Snacks.py",type="primary")
    st.link_button("Order here", "STREAMLIT/pages/3_Order_Items.py",type="primary")

