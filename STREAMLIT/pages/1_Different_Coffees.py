import streamlit as st
import time
st.set_page_config(page_title="Coffee ,Coffee",layout="wide",initial_sidebar_state="collapsed")
st.header("Here are different types of coffee for you to try :coffee:", divider="green")
with st.spinner('Please Wait...'):
    time.sleep(1)
# st.success('Done!')
# st.sidebar.header("You are viewing _a coffee_ page ")
col1, col2 = st.columns(2)

with col1:
    st.image("STREAMLIT/pages/Real.jpg")
    st.markdown("#### Dalgona Coffee - ₹160")
    st.write("Instant coffee, sugar , milk and anyway this frothy drink, known as dalgona coffee, might just be your new favourite caffeine kick ")
    st.markdown("#### Iced Macchiato - ₹155")
    st.write("two handfuls of ice, milk, vanilla syrup, 2 shots espresso, caramel sauce")
    st.markdown("#### Iced Latte - ₹175")
    st.write("2 espresso shots, sugar/honey/maple syrup, whole milk")
    st.markdown("#### Macchiato - ₹150")
    st.write("Ideal for breakfast, brunch or whenever you need a pick-me-up")
    st.markdown("#### Mocha - ₹169")
    st.write("Ground espresso, milk, drinking chocolate.")
    
with col2:
    # st.header("Lavanya Nair")
    st.markdown("#### French press coffee - ₹159")
    st.write("We use French coffee press maker, coffee of any roast and add filtered water if necessary, with Coffee grinder as a must")
    st.markdown("#### Americano - ₹139")
    st.write("1-shot for a mug and 2-shot for a latte mug according to you, using espresso roast coffee, add the two into the boiling water.")
    st.markdown("#### Cappucino - ₹139")
    st.write("One espresso pod or ground espresso as per requirement, with milk , served hot with cocoa powder.")
    st.markdown("#### Flat White - ₹139")
    st.write("One espresso pod or ground espresso as per requirement, with milk , served hot ")
    st.markdown("#### Latte - ₹169")
    st.write("One espresso pod or ground espresso as per requirement, with milk , served hot in large cup, 300-350ml capacity")
    st.image("STREAMLIT/pages/white.jpg")
    
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("Welcome Page", "STREAMLIT/Home",type="primary")
with col2:
    st.link_button("Yum, Yum food", "STREAMLIT/pages/2_Different_Snacks",type="primary")
with col3:
    st.link_button("Order here", "STREAMLIT/pages/3_Order_Items",type="primary")


# import time as t
# st.image("cloud.jpg")
# st.title("welcome to my first py web")
# st.header("machine learning")
# st.subheader("linear regression")
# st.info("Information")
# st.warning("Danger! Work in progress, watch your step!")
# st.write("employee name")
# st.write(range(50))
# st.error("wrong password")
# st.markdown("# Lavanya")
# st.markdown("## Lavanya")
# st.markdown(":moon:")
# st.text("Lavanya as a caption")
# st.caption("Caption is here ( real one )")
# st.latex(r''' a+b x^2+c ''')
# st.checkbox("Login")
# st.button("check")
# st.radio("gender please?", ["male","female","other"])
# st.selectbox("Pick a color",["pink","blue","orange"])
# st.select_slider("Rating",["5","4","3","2","1"])
# st.text_input("enter your email address")
# st.date_input("opening")
# st.time_input("hey whats the time?")
#textarea
# st.file_uploader("Upload a beautifule file :)")
# st.color_picker("Pick a lovely color")
# st.progress(90)
# with st.spinner("Chamshimanyo!!"):
#     t.sleep(2)

# st.balloons()
# st.sidebar.text("Hello side :)")

# import pandas as pd
# import numpy as np
# data = pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
# st.bar_chart(data)
# st.line_chart(data)
# st.area_chart(data)