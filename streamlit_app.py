import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError
#defining functions
def get_fruityvice_data(selected_fruit):
    fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+selected_fruit)
    fruityvice_normalized=pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
def get_fruitloadList():
    with my_snowCnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
st.header('Fruityvice Application\'s')
st.title("Get Fruit list")
if st.button('Click Here'):
        my_snowCnx=snowflake.connector.connect(**st.secrets["snowflake"])
        mydata_rows=get_fruitloadList()
        st.dataframe(mydata_rows)
