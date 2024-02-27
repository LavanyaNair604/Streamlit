import streamlit as st
import time
st.set_page_config(page_title="Snacks , Food",layout="wide",initial_sidebar_state="collapsed")
st.header("Snackity Snacks :cookie:", divider="green")
with st.spinner('Please Wait...'):
    time.sleep(1)
col1, col2 = st.columns(2)

with col1:
    st.image("STREAMLIT/pages/snack.jpg")
    st.markdown("#### Pop Tarts - ₹120")
    st.write("""Made with All purpose flavour,granulated sugar, cinnamon, honey, some strawberry preserves and alot of **LOVE**""")
    st.markdown("#### Vegan Biscotti - ₹111")
    st.write("""An all purpose flour, unsweetened milk, ganulated sugar, cinnamon, chocolate chips, vanilla extract and chopped pecans.""")
    st.markdown("#### Muffins - ₹50")
    st.write("""An all purpose flour, canberries, avocados, orange juice, orange zest. Also optional toppings like white or brown sugar, butter.""")
    
with col2:
    st.markdown("#### Ham Pizza Snacks - ₹140")
    st.write(
    """Spraying cookie sheet with nonstick spray. Biscuits and flatten on cookie sheet are separated with sauce on each.
    Topped with Ham and cheese baked in the oven and served hot.""")
    st.markdown("#### Nutella churro donut holes - ₹150")
    st.write("""Using pure Vanilla extract , fresh milk and all time favourite _Nutella_ we make our nutella churos donut holes.""")
    st.markdown("#### Pancakes - ₹139")
    st.write("""Pouring evenly sized batter into the pan is hard but we do it all with love for you.Flipping to the other side when its beautiful golden brown colour is all that take.""")
    st.markdown("#### Bagels - ₹110")
    st.write("""**Yeast** allows the dough to rise, for a dense and chewy texture a high protein flour is necessary. We serve this with some sprinkled brown sugar.""")
    st.image("STREAMLIT/pages/muff.jpg")

col1, col2, col3,col4= st.columns(4)
with col1:
    st.page_link("Home.py", label=":green[Home]",icon = "🏚️")
    
with col2:
    st.page_link("pages/1_Different_Coffees.py", label=":green[Our coffee collection]",icon = "☕")
with col3:
    st.page_link("pages/3_Order_Items.py", label=":green[Order Items]",icon = "📝") 
with col4:
    st.page_link("pages/4_Talk_with_me.py", label=":green[Your assistant 'Green']",icon = "🤖")
# st.sidebar.header("You are viewing the _about page_ ")
