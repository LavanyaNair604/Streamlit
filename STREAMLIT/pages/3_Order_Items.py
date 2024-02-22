import streamlit as st
from fpdf import FPDF
from datetime import date
import time
import base64
st.set_page_config(page_title="Order your items",layout="wide",initial_sidebar_state="collapsed")
cofe = {'French press coffee': 159, 'Americano':139,'Cappucino':139,'Flat White':139,'Latte':169,'Dalgona Coffee':160,'Iced Macchiato':155,'Iced Latte':175,'Macchiato':150,'Mocha':169}
snak = {'Ham Pizza Snacks': 140,'Nutella churro donut holes':150, 'Pancakes':139,'Bagels':110,'Pop Tarts': 120,'Vegan Biscotti':111,'Muffins':50}
st.header("Order your Items and get your receipt :sparkles:", divider="green")
with st.spinner('Please Wait...'):
    time.sleep(1)
st.markdown("#### Choose your coffee! :coffee:")
# coffee
def calculate_total_fare_coffee(selected_items, cofe):
    total_fare = sum(cofe[item] for item in selected_items)
    return total_fare

    # snacks
def calculate_total_fare_snacks(selected_items, cofe):
    total_fare = sum(snak[item] for item in selected_items)
    return total_fare
selected_items = st.multiselect('Select items:', list(cofe.keys()))
st.write('Selected Coffee:', selected_items)
total_fare = calculate_total_fare_coffee(selected_items, cofe)
st.write('Coffee Fare:', total_fare)
count = len(selected_items)
    
st.markdown("#### Choose your snacks! :cookie:")
selected_item = st.multiselect('Select items:', list(snak.keys()))
st.write('Selected Snacks:', selected_item)
total_fares = calculate_total_fare_coffee(selected_item, snak)
st.write('Snacks Fare:', total_fares)
today = date.today()
# st.write(" Coffee and Snacks Fare : ",total)
from fpdf import FPDF
pdf = FPDF()
def title():
    pdf.set_font('Arial', '', 12)
    pdf.cell(180, 10, txt="Cheruby Greens Cafe",ln=1, align="C")

def generate_pdf(customer_name, total):
    pdf.add_page()
    pdf.set_font_size(12)
    title()
    pdf.cell(180, 10, txt="Receipt",ln=1, align="C")
    pdf.ln()
    pdf.cell(50, 10, txt=f"Customer Name -  {customer_name}",ln=1, align="L")
    pdf.cell(50, 10, txt=f"Date - {today}",ln=1, align="L")
    pdf.ln()
    pdf.cell(50, 10, txt=f"Items",ln=0, align="L")
    pdf.cell(40, 10, txt=f"Item Fare",ln=0, align="C")
    # pdf.cell(40, 10, txt=f"Snacks Fare",ln=0, align="R")
    pdf.cell(60, 10, txt=f"Total",ln=1, align="R")
    pdf.ln()
    # Add details like date, customer name, etc.
    for key, value in cofe.items():
        if key in selected_items:
            pdf.cell(50, 10, txt=f"{key} (coffee)", ln=0,align="L")
            pdf.cell(50, 10, txt = f"{value}",align="C",ln=1)
    pdf.ln()
    # return pdf.output(dest="S").encode("latin-1")

    for key, value in snak.items():
        if key in selected_item:
            pdf.cell(50, 10, txt=f"{key} (snacks)", ln=0,align="L")
            pdf.cell(50, 10, txt = f"{value}",align="C",ln=1)
    pdf.ln()
    pdf.line(20, 32, 190, 32)
    pdf.cell(0, 10, txt=f"{total:.2f}", ln=1, align="R")
    # pdf.cell(0, 10, txt=f"Snacks Total: {total_fares:.2f}", ln=1, align="R")
    # pdf.cell(190, 30, txt=f"Coffee and Snacks Total: {total:.2f}", ln=1, align="R")
    return pdf.output(dest="S").encode("latin-1")




def download():
    pdf_data = generate_pdf(customer_name, total)
    b64 = base64.b64encode(pdf_data)
    progress_text = "Downloading your receipt.... Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    html = f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="receipt.pdf">View your receipt here</a>'
    st.markdown(html, unsafe_allow_html=True)

customer_name = st.text_input("Customer Name")
total = total_fare + total_fares


# Download button
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

clicked = st.button('Download')


if clicked and (len(selected_items) == 0) and (len(selected_item) > 0):
    if customer_name is None or customer_name == "":
        # st.session_state.clicked = True
        st.error("Enter your name please?")
    else:
        st.session_state.clicked = True
        st.info('Try our coffee next time you order!', icon="😋")
        st.success('Receipt Downloaded successfully!', icon="✅")
        download()

elif clicked and (len(selected_items) > 0) and (len(selected_item) > 0):
    if customer_name is None or customer_name == "":
        # st.session_state.clicked = True
        st.error("Enter your name please?")
    else:
        st.session_state.clicked = True
        st.success('Receipt Downloaded successfully!', icon="✅")
        download()
        st.snow()
    
elif clicked and (len(selected_item) == 0) and (len(selected_items) > 0):
    if customer_name is None or customer_name == "":
        # st.session_state.clicked = True
        st.error("Enter your name please?")
    else:
        st.session_state.clicked = True
        st.info('Try some snacks next time you order!', icon="😍")
        st.success('Receipt Downloaded successfully!', icon="✅")
        download()

elif clicked and (len(selected_items) == 0) and (len(selected_item) == 0):
        st.session_state.clicked = True
        st.info("Only receipt? Choose a snack or a coffee please!",icon = "😞")
    
else:
    pass
    
    
