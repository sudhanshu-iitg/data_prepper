import requests
import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_extras.switch_page_button import switch_page
from functions import *
from redis import Redis
import msgpack
from direct_redis import DirectRedis


r2 = DirectRedis(host='localhost', port=6379)

# df2= pd.read_excel('test.xlsx')
COLUMN_NAMES = ["id","name","slug",	"permalink"	,"date_created","date_created_gmt","date_modified","date_modified_gmt","type","status","featured","catalog_visibility","description","short_description","sku","price","regular_price","sale_price","date_on_sale_from","date_on_sale_from_gmt","date_on_sale_to","date_on_sale_to_gmt","on_sale","purchasable","total_sales","virtual","downloadable","downloads","download_limit","download_expiry","external_url","button_text","tax_status","tax_class","manage_stock","stock_quantity","backorders","backorders_allowed","backordered","low_stock_amount","categories"]
# df2 = pd.DataFrame(columns=COLUMN_NAMES)
items = 0
redis_host = '127.0.0.1'
r = Redis(redis_host)

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

if st.button('Load creds'):
    st.session_state.woocom_key = "ck_1b8d39921fffd8f2a90c17445a0d898f1014911f"
    st.session_state.woocom_secret = "cs_8f7863cebc4f9c487fdbcc7f2b5dcfdedfecac12"
    st.session_state.woocom_url = "https://www.hanfpost.ch"



    st.write(check())
# if st.button('Generate complete file'):

#     try:
#         CONSUMER_KEY = st.session_state.woocom_key
#         CONSUMER_SECRET = st.session_state.woocom_secret
#         url=st.session_state.woocom_url
#         url1 = url+"/wp-json/wc/v3/products"
#         allProducts = pd.DataFrame()
#         page = 1

#         while page != False:
#             print(page)
#             para = {"per_page":100,"page":page}
#             products =requests.get(url1, auth=(CONSUMER_KEY, CONSUMER_SECRET),params=para)

#             if (len(products.json())>0) :
#                 st.info(str(len(products.json())) + " products added")
#                 df3 = pd.DataFrame(products.json())
#                 allProducts=pd.concat([allProducts,df3])
#                 page=page+1

#                 page= False
#             else :
#                 page = False
#         df2 = pd.DataFrame(allProducts)
#         # js = df2.to_json()
#         # js = str(js)
#         # r.set('data',js)
#         r2.set('df', df2) 

        
#     except Exception as e:
#         st.write("No can do, error came" + str(e))
        
# st.dataframe(df2.astype(str))
# if st.button('Save file'):
    
#     js = df2.to_json()
#     st.write(js)
#     st.dataframe(df2.astype(str))
#     r.set('data',"js")
#     st.session_state.data = df2

