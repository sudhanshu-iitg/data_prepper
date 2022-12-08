import requests
import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_extras.switch_page_button import switch_page
from functions import *
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import streamlit as st
from redis import Redis
import msgpack
from direct_redis import DirectRedis
from functions import *
import json
import os


# COLUMN_NAMES = ["id","name","slug",	"permalink"	,"date_created","date_created_gmt","date_modified","date_modified_gmt","type","status","featured","catalog_visibility","description","short_description","sku","price","regular_price","sale_price","date_on_sale_from","date_on_sale_from_gmt","date_on_sale_to","date_on_sale_to_gmt","on_sale","purchasable","total_sales","virtual","downloadable","downloads","download_limit","download_expiry","external_url","button_text","tax_status","tax_class","manage_stock","stock_quantity","backorders","backorders_allowed","backordered","low_stock_amount","categories"]
r2 = DirectRedis(host='localhost', port=6379)
redis_host = '127.0.0.1'
r = Redis(redis_host)
try:
    df2 = pd.read_csv (r"1.csv")
except:
    df2 = pd.DataFrame()
try:
    with open('sample3.json', 'r') as openfile:
 
    # Reading from json file
        json_object = json.load(openfile)
        base_list = json_object
except:
    base_list = ["id","name","type","status","description","short_description","sku","price","regular_price","stock_quantity" ]
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
# st.write(json_object)
# st.write(aList)
# st.write(type(json_object))

if st.button('load data'):
    # type(r2.get('df'))
    
    # sample = r.get('data').decode()
    # df3= pd.read_json(sample)
    st.write(df2.astype(str))
    # df2 = df3

df_xlsx = to_excel(df2)
st.download_button(label='📥 Download Complete file',
                                data=df_xlsx ,
                                file_name= 'test.xlsx')
try:
    df_xlsx1 = to_excel(df2[base_list])
    st.download_button(label='📥 Download base file',
                                data=df_xlsx1 ,
                                file_name= 'test.xlsx')
except:
    st.write('need to reset')


if st.button('reset'):
    
    if os.path.exists("sample3.json"):
        os.remove("sample3.json")
    if os.path.exists("1.csv"):
        os.remove("1.csv")
    
# st.write(base_list)