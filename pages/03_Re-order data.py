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


# r2 = DirectRedis(host='redis', port=6379)
# redis_host = '127.0.0.1'
# r = Redis(redis_host)
try:
    # df2= r2.get('df')
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
list_columns = ["sku"]
list_attributes = ["sku","attributes"]
list_images = ["sku","images"]
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

st.title("Step 4: Re-order data")
st.write(base_list)
st.write(type(base_list))
if st.button('load data'):
    # type(r2.get('df'))
    # df3 = r2.get('df')
    df3 = pd.read_csv (r"1.csv")
    # sample = r.get('data').decode()
    # df3= pd.read_json(sample)
    st.write(df3.astype(str))
    df2 = df3
    # df2= st.session_state.data
st.dataframe(df2[['sku','categories']].astype(str))
if st.button('Sort Categories'):
    try:
        for index, row in df2.iterrows():
            image = row["categories"]
            image = str(image)
            image_1 = image.replace("'", '"')
            try:
                js = json.loads(image_1)
            except Exception as e:
                ee = ""
            # js = json.dumps(js)
            count = 0
            for item in js:
                column_name = 'Category '+ str(count)
                df2.loc[index,column_name ] =item['name']
                list_columns = list_columns + [column_name] if column_name not in list_columns else list_columns
                base_list = base_list + [column_name] if column_name not in base_list else base_list
                count=count+1
        df2.to_csv("1.csv")
        my_json = json.dumps(base_list)
        with open("sample3.json", "w") as outfile:
            outfile.write(my_json)
        
        # r2.set('list',base_list)

    except Exception as e:
        st.write(e)
st.dataframe(df2[list_columns].astype(str))
# st.dataframe(df2[list_attributes].astype(str))
        # print(link)
if st.button('Sort Attributes'):
    for index, row in df2.iterrows():
        image = row["attributes"]
        # print(image)
        if image=="[]":
            ee=""
        else:
            image = str(image)
            image_1 = image.replace("True", '"true"')
            image_1 = image_1.replace("False", '"false"')
            image_1 = image_1.replace("'", '"')
            
            print(image_1)
            try:
                js = json.loads(image_1)
                print('1')
            except Exception as e:
                print(e)
                print('2')
            # js = json.dumps(js)
            count = 0
            print(js)
            for item in js:
                column_name = 'attribute name '+ str(count)
                column_name_1 = 'attribute value '+ str(count)
                
                try:
                    df2.loc[index,column_name_1 ] =item['options']
                    df2.loc[index,column_name ] =item['name']

                except Exception as e:
                    
                    ee=''
                list_attributes = list_attributes + [column_name] if column_name not in list_attributes else list_attributes
                list_attributes = list_attributes + [column_name_1] if column_name_1 not in list_attributes else list_attributes
                base_list = base_list + [column_name] if column_name not in base_list else base_list
                base_list = base_list + [column_name_1] if column_name_1 not in base_list else base_list
                count=count+1
    df2.to_csv("1.csv")
    my_json = json.dumps(base_list)
    with open("sample3.json", "w") as outfile:
            outfile.write(my_json)  
st.dataframe(df2[list_attributes].astype(str))


st.dataframe(df2[['sku','images']].astype(str))
if st.button('Sort images'):
    for index, row in df2.iterrows():
        image = row["images"]
        image = str(image)
        image_1 = image.replace("'", '"')
        try:
            js = json.loads(image_1)
        except Exception as e:
            ee = ""
        # js = json.dumps(js)
        count = 0
        for item in js:
            column_name = 'image '+ str(count)
            df2.loc[index,column_name ] =item['src']
            list_images = list_images + [column_name] if column_name not in list_images else list_images
            base_list = base_list + [column_name] if column_name not in base_list else base_list
            count=count+1
    df2.to_csv("1.csv")
    my_json = json.dumps(base_list)
    with open("sample3.json", "w") as outfile:
            outfile.write(my_json)
st.dataframe(df2[list_images].astype(str))
# st.dataframe(df2[[base_list]].astype(str))

df_xlsx = to_excel(df2)
st.download_button(label='📥 Download Complete file',
                                data=df_xlsx ,
                                file_name= 'test.xlsx')

# if st.button('show'):
#     try:
#         df2= r2.get('df')
#         df_xlsx1 = to_excel(df2[[base_list]])
#         st.download_button(label='📥 Download base file',
#                                     data=df_xlsx1 ,
#                                     file_name= 'test.xlsx')
#     except Exception as e:
#         st.write(e)
