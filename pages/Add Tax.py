import requests
import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_extras.switch_page_button import switch_page
from functions import *

df2= pd.read_excel('test.xlsx')
df3= pd.read_excel('taxes.xlsx')
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

st.title("Step 2: add tax from WooCommerce")

if st.button('Generate complete file'):
    for index,row in df2.iterrows():

        tax_class= row["tax_class"]
        if tax_class!=tax_class:
             print(index)
             try:
                 df2.loc[index,'woocom_tax']="No tax class in Woocommerce"
             except Exception as e:
                st.write(e)
        else:
            
            try:
                tax_row = df3.loc[df3["class"]==tax_class]
                df2.loc[index,'woocom_tax']=tax_row["rate"].values[0]
            except:
                df2.loc[index,'woocom_tax']="error"
    test = df2[['sku',"woocom_tax"]].astype(str)
    st.dataframe(test)


