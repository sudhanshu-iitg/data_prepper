
import requests
import pandas as pd
from io import StringIO
from requests_oauthlib import OAuth1Session
import json
import re
import ast
import streamlit as st

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
    response = requests.get(url1, auth=(CONSUMER_KEY, CONSUMER_SECRET),params=para)
    if(response.status_code==200):
        url1=url1
        return True
    else:
        url1=url1+"?consumer_key="+CONSUMER_KEY+"&consumer_secret="+CONSUMER_SECRET
        
        response = requests.get(url1, auth=(CONSUMER_KEY, CONSUMER_SECRET),params=para)
        if(response.status_code==200):
            return True
            st.session_state.woocom_url = url1
        else :
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