import streamlit as st
import pandas as pd
import requests 
import numpy as np 

st.title('Item recommendation')
users= pd.read_csv('clicks_df.csv')
users=users['user_id']
top_n = pd.read_pickle('top_n.pkl')
st.header('Item Recommendation System')
list_ = np.random.choice(users,1000)

option = st.selectbox(
    'Select a user', list_)

if st.button('Show Recommendation'):
      url='https://testdibs.azurewebsites.net/api/http_trigger_recommendation?userId={}'.format(option)
      res= requests.get(url=url)
      res.text












