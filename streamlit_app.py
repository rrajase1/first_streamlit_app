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
  
streamlit.header('Fruityvice Application\'s')
streamlit.title("Get Fruit list")

#Snowflake connection

my_snowCnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_snowCnx.cursor()
my_cur.execute("select current_user(),current_account(),current_region()")
mydata_row=my_cur.fetchone()
streamlit.text("Snow Flake Data:")
streamlit.text(mydata_row)

## don't run anything after here.
#streamlit.stop()
streamlit.text("commencted lines")

my_cur.execute("select * from fruit_load_list")
mydata_row=my_cur.fetchone()
streamlit.text("Fruit Load List - First one:")
streamlit.text(mydata_row)
streamlit.text("Dataframe:")
streamlit.dataframe(mydata_row)

my_cur.execute("select * from fruit_load_list")
mydata_row=my_cur.fetchall()
streamlit.text("Fruit Load List - All:")
streamlit.text(mydata_row)
streamlit.text("Dataframe:")
streamlit.dataframe(mydata_row)

#Adding textbox
streamlit.header("Pick yor Fruit")
user_text=streamlit.text_input("Pick yor Fruit")
streamlit.write("Thanks for adding:",user_text)

#my_cur.execute("insert into fruit_load_list values('from streamlit')")

## new section to display fruitywise api advice
streamlit.header('Fruitywise fruit advice:')
#user_text=streamlit.text_input("Fruit to get advice",'kiwi')
try:
  user_text=streamlit.text_input("Fruit to get advice")
  if not user_text:
      streamlit.error('Please select a fruit')
  else:
    # non function method start
    #fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+user_text)
    #fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    #streamlit.dataframe(fruityvice_normalized)
    # non function method end
    
    #function method start
      backfrom_function=get_fruityvice_data(user_text)
      streamlit.dataframe(backfrom_function)
    #function method end
except URLError as e:
  streamlit.error()
