import streamlit as st
import requests


st.markdown('''
Please complete the form to see the estimated fare.
''')


pickup_datetime = st.text_area("date and time", '2013-07-06 17:18:00')
pickup_longitude = st.text_area("pickup longitude",'-73.950655')
pickup_latitude = st.text_area("pickup latitude",'40.783282')
dropoff_longitude = st.text_area("dropoff longitude",'-73.984365')
dropoff_latitude = st.text_area("dropoff latitude", '40.769802')
passenger_count = st.text_area("passenger count", '2')

url = 'https://taxifare.lewagon.ai/predict'

params = {
    "pickup_datetime": pickup_datetime,  # 2013-07-06 17:18:00
    "pickup_longitude": pickup_longitude,    # -73.950655
    "pickup_latitude": pickup_latitude,     # 40.783282
    "dropoff_longitude": dropoff_longitude,   # -73.984365
    "dropoff_latitude": dropoff_latitude,    # 40.769802
    "passenger_count": passenger_count
}

response = requests.get(url, params=params).json()

if st.button('Submit'):
    st.write('Fare:', response["fare"])
else:
    st.write('Please submit to see the fare')
