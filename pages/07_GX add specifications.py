import requests
import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_extras.switch_page_button import switch_page
from functions import *
from direct_redis import DirectRedis
from redis import Redis


r2 = DirectRedis(host='localhost', port=6379)
redis_host = '127.0.0.1'
r = Redis(redis_host)
try:
    df2= r2.get('df')
except:
    df2 = pd.DataFrame()
try:
    base_list = r2.get('list')
except:
    base_list = ["id","name","type","status","description","short_description","sku","price","regular_price","stock_quantity" ]
# df2= pd.read_excel('test.xlsx')
df3 = pd.read_excel("Gx-attibutes.xlsx")
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
    # df2["input"] = "vaue"
    st.dataframe(df2[['sku','categories','gx-category']].astype(str))

if st.button('add attributes'):
    for index, row in df2.iterrows():
        category = row["gx-category"]
        st.write("category "+category)
        for index,row in df3.iterrows():
                if row["Produkttyp"] == category:
                    
                    if row["Gatekeeper"] == "X":
                        # st.write(row["Eigenschaft"])
                        df2[row["Eigenschaft"]] = None
                        base_list = base_list + [row["Eigenschaft"]] if row["Eigenschaft"] not in base_list else base_list
                    elif row["Filter"] == "X":
                        # st.write("Filter " + row["Eigenschaft"])
                        df2[row["Eigenschaft"]] = None
                        base_list = base_list + [row["Eigenschaft"]] if row["Eigenschaft"] not in base_list else base_list
    r2.set('df', df2)
    st.info("specification columns added")

if st.button('Run this'):
    for index, row in df2.iterrows():
        category = row["gx-category"]
        # st.write("category "+category)
        df4 = df3.loc[df3['Produkttyp'] == category,:]
        for index1,row1 in df4.iterrows():
                    if row1["Gatekeeper"] == "X":
                        # st.write(row["Eigenschaft"])
                        df2.loc[index,row1["Eigenschaft"] ] = "x"
                    elif row1["Filter"] == "X":
                        # st.write("Filter " + row["Eigenschaft"])
                        df2.loc[index,row1["Eigenschaft"] ] = "x"
    r2.set('df', df2)
