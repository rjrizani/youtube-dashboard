import streamlit as st

st.title("About This Dashboard")
st.markdown("""
This dashboard allows users to analyze YouTube channels by uploading a CSV file containing channel data. 
Explore insights on subscriber count and video count, along with visualizations to better understand trends.
""")

# Connect with Developer Button
st.markdown("""
<style>
.button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
}
</style>
<a href="https://rjscrapy.pythonanywhere.com/developer" target="_blank" class="button">Connect with Developer</a>
""", unsafe_allow_html=True)