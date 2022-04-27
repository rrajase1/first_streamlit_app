import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError
#defining functions
def get_fruityvice_data(selected_fruit):
    fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+selected_fruit)
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
st.header('Fruityvice Application\'s')
st.title("Get Fruit list")

