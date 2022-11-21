import streamlit as st

st.set_page_config(page_title="Vitamin Shoppe Demo", page_icon="🏀", layout="centered")

from utils import gui

# gui.icon("🏀")

st.image(
    "https://s3.amazonaws.com/appforest_uf/f1645050160993x340144886538052540/Cerebro%20Logo%20Black-J8AG.png",
    width=300, # Manually Adjust the width of the image as per requirement
   )

# Make sure session state is preserved
for key in st.session_state:
    st.session_state[key] = st.session_state[key]

st.title("Cerebro Roadmap")
st.sidebar.info("Choose a page")
st.markdown(
    """
This front-end can be used to create/monitor product enhancemants and submit any bugs. 
### Get started!
👈 Select a page in the sidebar
    """
)
