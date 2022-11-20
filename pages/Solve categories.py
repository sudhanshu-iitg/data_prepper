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

df2= st.session_state.data
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

st.title("Step 2: solve categories")
st.dataframe(df2[['sku','categories']])
if st.button('Sort Categories'):
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
            column_name = 'category'+ str(count)
            df2.loc[index,column_name ] =item['name']
            list_columns = list_columns + [column_name] if column_name not in list_columns else list_columns
            count=count+1

st.dataframe(df2[list_columns])
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
                column_name = 'attribute name'+ str(count)
                column_name_1 = 'attribute value'+ str(count)
                
                try:
                    df2.loc[index,column_name_1 ] =item['options']
                    df2.loc[index,column_name ] =item['name']

                except Exception as e:
                    
                    ee=''
                list_attributes = list_attributes + [column_name] if column_name not in list_attributes else list_attributes
                list_attributes = list_attributes + [column_name_1] if column_name_1 not in list_attributes else list_attributes
                count=count+1
        

st.dataframe(df2[list_attributes])

st.dataframe(df2[['sku','images']])
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
            list_columns = list_images + [column_name] if column_name not in list_images else list_images
            count=count+1

st.dataframe(df2[list_images])