import requests
import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_extras.switch_page_button import switch_page
from functions import *

df2= pd.read_excel('test.xlsx')
bexio_tax_list= pd.read_excel('taxlist.xlsx')
bexio_data= pd.read_excel('snus-bexio_11.xlsx')
list_columns = ["sku"]
list_attributes = ["sku","attributes"]
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

st.title("Step 2: solve categories")


st.dataframe(df2[list_columns])
        # print(link)
if st.button('Add tax'):
    for index,row in df2.iterrows():
        sku= row["sku"]
        # print(tax_id)
        try:
            roow = bexio_data.loc[bexio_data["intern_code"]==str(sku)]
        except:
            st.write("3")
            st.write(index)
        # print(index)
        # print(roow['intern_code'].values[0])
        # print(sku)
        try:
            tax_id = roow["tax_id"].values[0]
            tax_roow = bexio_tax_list.loc[bexio_tax_list["id"]==tax_id]
            df2.loc[index,'bexio_tax']=str(tax_roow["value"].values[0])
        except:
            df2.loc[index,'bexio_tax']="Not found in Bexio"
        
       
    
        

st.dataframe(df2[['sku','bexio_tax']])