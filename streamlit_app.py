import streamlit as st

st.set_page_config(page_title="Vitamin Shoppe Demo", page_icon="🌀", layout="centered")

from utils import gui

# gui.icon("🌀")

st.image(
    "https://www.newhope.com/sites/newhope360.com/files/vitaminshoppe-logo-2018-promo.png",
    width=300, # Manually Adjust the width of the image as per requirement
   )

# Make sure session state is preserved
for key in st.session_state:
    st.session_state[key] = st.session_state[key]

st.title("Welcome to the VS Customer Insights app!")
st.sidebar.text(f"Account: {st.secrets.sf_usage_app.account}")
st.sidebar.info("Choose a page!")
st.markdown(
    """
This app provides insights on a Vitamin Shoppe's customers
### Get started!
👈 Select a page in the sidebar!
    """
)
