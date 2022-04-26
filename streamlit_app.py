import streamlit
import pandas
import requests
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
