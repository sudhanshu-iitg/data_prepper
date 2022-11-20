import requests
import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_extras.switch_page_button import switch_page
from functions import *

df2= pd.read_excel('test.xlsx')

st.set_page_config(
     page_title="Step 2 - Generate complete file",
     page_icon="https://uploads-ssl.webflow.com/6278f3c8ca098b4b29fd9609/62b5aeb5966e384261f03b06_favicon-32x32.png",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)

st.title("Step 2: Generate complete file")

if st.button('Generate complete file'):
    CONSUMER_KEY = st.session_state.woocom_key
    CONSUMER_SECRET = st.session_state.woocom_secret
    url=st.session_state.woocom_url

    url1 = url+"/wp-json/wc/v3/products"
    allProducts = pd.DataFrame()
    page = 1

    while page != False:
        print(page)
        para = {"per_page":100,"page":page}
        products =requests.get(url1, auth=(CONSUMER_KEY, CONSUMER_SECRET),params=para)

        if (len(products.json())>0) :
            df3 = pd.DataFrame(products.json())
            allProducts=pd.concat([allProducts,df3])
            page=page+1
            print(len(products.json()))
            # page = False
            
        else :
            page = False
        
    df2 = pd.DataFrame(allProducts)
    st.dataframe(df2.astype(str))
if st.button('Save file'):

    st.session_state.data = df2

