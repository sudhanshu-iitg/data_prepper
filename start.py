import requests
import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_extras.switch_page_button import switch_page
from requests_oauthlib import OAuth1Session
from functions import *

st.set_page_config(
     page_title="Step 1 - Product Data Prep",
     page_icon="https://uploads-ssl.webflow.com/6278f3c8ca098b4b29fd9609/62b5aeb5966e384261f03b06_favicon-32x32.png",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)   
st.title("Step 1️⃣: Connect / Upload your  Data")

woocom_key = st.text_input("The Woocommerce key", "ck_####")
woocom_secret = st.text_input("The Woocommerce secret", "cs_###")
woocom_url = st.text_input("The Woocommerce url", "http://example.com")
# CONSUMER_KEY = "ck_1b8d39921fffd8f2a90c17445a0d898f1014911f"
# CONSUMER_SECRET = 'cs_8f7863cebc4f9c487fdbcc7f2b5dcfdedfecac12'

if st.button('Save credentials'):
    st.session_state.woocom_key = woocom_key
    st.session_state.woocom_secret = woocom_secret
    st.session_state.woocom_url = woocom_url
    st.session_state.credential_saved = True 



# oauthRequest = OAuth1Session(CONSUMER_KEY,
#                     client_secret=CONSUMER_SECRET)

if st.button('Check credentials'):
    try:
        st.text(check())
    except Exception as e:
        st.text(e)
    # switch_page("Step")
    
    





























