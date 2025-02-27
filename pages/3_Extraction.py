import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.extraction import get_comments


st.title('Youtube Data Extraction')
st.markdown('This app extracts comments from a youtube video')


#table df

input_id = st.text_input('Enter the video ID (e.g. -3QV0vhCeHg)')
st.write('The video ID is:', input_id)

number = st.number_input('Enter the number of comments to extract', min_value=1, max_value=100)
st.write('The number of comments to extract is:', number)

extract = st.button('Extract Comments')
if extract:
    df = get_comments(videoId=input_id)
    st.write('Comments extracted:')
    st.dataframe(df)
    st.write('---')
    st.write('Go to Sentiment Analysis of Comments')
else:
    st.write('Click the button to extract comments')


