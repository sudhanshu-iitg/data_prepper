import requests
import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_extras.switch_page_button import switch_page
from functions import *
from direct_redis import DirectRedis

r2 = DirectRedis(host='localhost', port=6379)
try:
    df2= r2.get('df')
except:
    df2 = pd.DataFrame()
try:
    df3= r2.get('df_tax')
except:
    df3 = pd.DataFrame()
# df3= pd.read_excel('taxes.xlsx')
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

if st.button("fetch tax list"):
    CONSUMER_KEY = st.session_state.woocom_key
    CONSUMER_SECRET = st.session_state.woocom_secret
    url=st.session_state.woocom_tax_url
    # st.write(url)
    # url3 = "/wp-json/wc/v3/taxes"
    # url2= url+url3
    taxes =requests.get(url, auth=(CONSUMER_KEY, CONSUMER_SECRET)).json()
    df3=pd.DataFrame(taxes)
    r2.set("df_tax",df3)

    st.write(df3)

if st.button('Add tax from Woocommerce'):
    df3 = r2.get("df_tax")
    for index,row in df2.iterrows():

        tax_class= row["tax_class"]
        if tax_class!=tax_class:
             print(index)
             try:
                 df2.loc[index,'woocom_tax']="No tax class in product"
             except Exception as e:
                st.write(e)
        else:
            
            try:
                tax_row = df3.loc[df3["class"]==tax_class]
                # st.write(df3)
                df2.loc[index,'woocom_tax']=tax_row["rate"].values[0]
            except Exception as e:
                # st.write(e)
                df2.loc[index,'woocom_tax']="No tax class in woocommerce"
    test = df2[['sku',"woocom_tax","tax_class"]].astype(str)
    r2.set('df', df2)
    st.dataframe(test)


