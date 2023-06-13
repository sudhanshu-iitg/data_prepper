
import pandas as pd
import streamlit as st
import requests
import time
from functions import *
# # Google Sheets API credentials
# scope = ['https://www.googleapis.com/auth/spreadsheets']
# creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
# client = gspread.authorize(creds)

# Streamlit app
df = pd.DataFrame()
def my_function(input_text):
    # Insert your function code here
    SHEET_NAME = 'Sheet1'
    url = f'https://docs.google.com/spreadsheets/d/{input_text}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    df = pd.read_csv(url)
    if 'df' not in st.session_state:
        st.session_state.df = df
    st.session_state.df = df
    st.write(df)
    return df
st.title('Specification generation from Google sheets')


# Retrieve data from Google Sheets
sheet_URL = st.text_input('Enter your google sheet ID.')
if 'df' not in st.session_state:
    headers = []
else:
    headers = list(st.session_state.df.columns)
# Convert data into a Pandas DataFrame
# SHEET_ID = '1uunHqpwUFiayPJPY-3vwrt4COYWqA7PO_y4BFegnylc'

if st.button('Fetch Data'):
    output = my_function(sheet_URL)
    headers = list(output.columns)
    
st.session_state.column = st.selectbox('Select the column containing descriptions', headers)
st.write('You selected:', st.session_state.column)
st.session_state.column1 = st.selectbox('Select the column containing descriptions', headers)
st.write('You selected:', st.session_state.column1)
# st.write(df)
if st.button('Do the Magic'):
    # output = my_function(sheet_URL)
    if 'df' not in st.session_state:
        st.write("no data found")
    else:
        df = st.session_state.df
        for index, row in df.iterrows():
            toast = st.empty()
            toast.success(index) 
            time.sleep(1)
            json = {
                "data": [ row[st.session_state.column],row[st.session_state.column1]] }
            url = "https://suds-0308-specification-generator.hf.space/run/predict"
            # headers = {"accept": "application/json","Content-Type": "application/json"}
            response = requests.post("https://suds-0308-specification-generator.hf.space/run/predict", json={
                "data": [
                    row[st.session_state.column]]})
            try:
                df.loc[index,"New Category -1" ] = response.json()['data'][2]['label']
                try:
                    # st.write(response.json()['data'])
                    items = response.json()['data'][1]['label'].split(",")
                    count = 1
                    for item in items:
                        if "[" in item:
                            item = item.split("[")[1]
                        if "]" in item:
                            item = item.split("]")[1]
                        if "NA" not in item and len(item)>0:
                            keys = item.split(":")
                            # st.write(count)
                            # st.write(len(item))
                            # count = count+1
                            try:
                                df.loc[index,"Specification key "+str(count) ] = keys[0]
                                df.loc[index,"Specification value "+str(count) ] = keys[1] 
                                count = count+1
                                
                            except Exception as e:
                                
                                st.write(e)
                                st.write(keys)
                                df_xlsx = to_excel(df)
                                st.download_button(label='📥 Download Generated file',
                                    data=df_xlsx ,
                                    file_name= 'file.xlsx')
                except Exception as e:
                    st.write(response.json())
                    st.write(e)
                    df_xlsx = to_excel(df)
                    st.download_button(label='📥 Download Generated file',
                                    data=df_xlsx ,
                                    file_name= 'file.xlsx')
            except Exception as e:
                st.write(response)
                df_xlsx = to_excel(df)
                st.download_button(label='📥 Download Generated file',
                                data=df_xlsx ,
                                file_name= 'file.xlsx')
            
        st.write(df)   # break
        df_xlsx = to_excel(df)
        st.download_button(label='📥 Download Generated file',
                                data=df_xlsx ,
                                file_name= 'file.xlsx')

# Display the DataFrame
# st.write(df)