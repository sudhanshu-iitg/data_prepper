
import requests
import pandas as pd
from io import StringIO
from requests_oauthlib import OAuth1Session
import json
import re
import ast
import streamlit as st
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.close()
    processed_data = output.getvalue()
    return processed_data


    
def check():
    
    CONSUMER_KEY = st.session_state.woocom_key
    CONSUMER_SECRET = st.session_state.woocom_secret
    url=st.session_state.woocom_url
    
    client = "prime"
    st.write(st.session_state)
    token = ""
    url1 = url+"/wp-json/wc/v3/products"
    page = 1
    para = {"per_page":1,"page":page}
    headers = {
    'User-Agent': 'Chrome v22.2 Linux Ubuntu',
}
    response = requests.get(url1, auth=(CONSUMER_KEY, CONSUMER_SECRET),params=para,headers=headers)
    if(response.status_code==200):
        url1=url1
        st.session_state.woocom_product_url = url1
        url2 = url +"/wp-json/wc/v3/taxes"
        st.session_state.woocom_tax_url = url2
        return True
    else:
        url1=url1+"?consumer_key="+CONSUMER_KEY+"&consumer_secret="+CONSUMER_SECRET
        
        response = requests.get(url1, auth=(CONSUMER_KEY, CONSUMER_SECRET),params=para,headers=headers)
        if(response.status_code==200):
            
            st.write(url1)
            st.session_state.woocom_product_url = url1
            url2 = url +"/wp-json/wc/v3/taxes?consumer_key="+CONSUMER_KEY+"&consumer_secret="+CONSUMER_SECRET
            st.session_state.woocom_tax_url = url2
            return True
        else :
            return False


def check_bexio():

    token = st.session_state.bexio_token
    
    url = "https://api.bexio.com/2.0/article"
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': "Bearer "+token,
        }
    params = {"limit":1}
    
    response = requests.request("GET", url, headers=headers, params=params)
    list=response.json()
    bexio_data = pd.DataFrame(list)
    if(response.status_code==200):
        # url1=url1
        return True
    else:
       return False


def generate():
    CONSUMER_KEY = "ck_e74a07a8ee74ace03ad00668079fcd8db374fca1"
    CONSUMER_SECRET = 'cs_ebbe2d93b4829597c0f7c769189075757cbf9740'
    
    url="https://www.primedrinks.ch"
    url1 = url+"/wp-json/wc/v3/products"
    allProducts = pd.DataFrame()
    page = 1

    while page != False:
        print(page)
        para = {"per_page":90,"page":page}
        products =requests.get(url1, auth=(CONSUMER_KEY, CONSUMER_SECRET),params=para)

        if (len(products.json())>0) :
            df3 = pd.DataFrame(products.json())
            allProducts=pd.concat([allProducts,df3])
            page=page+1
            print(len(products.json()))
            
        else :
            page = False
        
    df2 = pd.DataFrame(allProducts)
    return df2

def generate_base():
    list_columns = ["id","name","type","status","description","short_description","sku","price","regular_price","stock_quantity","images" ]
    df2 = pd.read_excel("test.xlsx")
    df3 = df2[list_columns]
    return df3

def add_tax():
    list_columns = ["id","name","type","status","description","short_description","sku","price","regular_price","stock_quantity" ]
    df2 = pd.read_excel("test.xlsx")
    df3 = df2[list_columns]
    return df3


def sort_data():
    list_columns = ["id","name","type","status","description","short_description","sku","price","regular_price","stock_quantity" ]
    df2 = pd.read_excel("test.xlsx")
    for index, row in df2.iterrows():
        image = row["images"]
        image = str(image)
        image_1 = image.replace("'", '"')
        js = json.loads(image_1)
        # js = json.dumps(js)
        count = 0
        for item in js:

            print(item['src'])
            # print(index)
            print(count)
            column_name = 'image '+ str(count)
            df2.loc[index,column_name ] =item['src']
            list_columns.append(column_name)
            count=count+1
    df3 = df2[list_columns]
    return df3