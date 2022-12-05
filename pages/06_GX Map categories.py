import requests
import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_extras.switch_page_button import switch_page
from functions import *
from direct_redis import DirectRedis
from redis import Redis

list_category = []

r2 = DirectRedis(host='localhost', port=6379)
redis_host = '127.0.0.1'
r = Redis(redis_host)
try:
    df2= r2.get('df')
    

except:
    df2 = pd.DataFrame()
df3 = pd.read_excel("Gx-categories.xlsx")
# df2= pd.read_excel('test.xlsx')
list = df3['Produkttyp'].unique()
def add_category(string):
    st.write(string)
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
option = ""
if st.button('Generate complete file'):
    df2["input"] = "vaue"
    st.dataframe(df2[['sku','categories','input']].astype(str))
st.write(option)
container = st.container()
def add_category(string,index):
    print(option)

for index, row in df2.iterrows():
        column_name = row["category0"]
        if column_name not in list_category:
            list_category = list_category + [column_name]
            col2,col3 = st.columns(2)
            
            with col2:
                st.write(row["category0"])
            with col3:
               option = st.selectbox(
        'Map the Galaxus category.',
        list,key=index)
            if option!=option:
                print("something")
            else:
                for index,row1 in df2.iterrows():
                    if row1["category0"]==row["category0"]:
                        df2.loc[index,'gx-category']=option
                        r2.set('df', df2)
