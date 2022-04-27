import streamlit
#import streamlit as st
import pandas
#import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('my streamlit title\'s')
streamlit.text('i can type anything here')
streamlit.text('as much as i like ')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list =my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect('Pick Your Fruits:',list(my_fruit_list.index),['Avocado','Grapes'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.json())
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#output to screen
streamlit.dataframe(fruityvice_normalized)

#Snowflake connection

my_snowCnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_snowCnx.cursor()
my_cur.execute("select current_user(),current_account(),current_region()")
mydata_row=my_cur.fetchone()
streamlit.text("Snow Flake Data:")
streamlit.text(mydata_row)

## don't run anything after here.
streamlit.stop()
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

my_cur.execute("insert into fruit_load_list values('from streamlit')")
