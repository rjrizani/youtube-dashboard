import streamlit as st
import pandas as pd

# Streamlit app
st.title("YouTube Channel Analysis")
st.markdown("""
## Dashboard Information

This dashboard analyzes YouTube channels based on their subscribers and video counts.

**CSV File Requirements:**
- **name**: Channel name
- **subscribers**: Number of subscribers
- **videos_count**: Number of videos
- **created_date**: Date when the channel was created

Upload a valid CSV file to view detailed summaries and visualizations below.
""")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the data from the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Convert 'created_date' to datetime format
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    df['subscribers'] = df['subscribers'].fillna(0)  # Replace NaN with 0 for analysis

    # Summarizing the data to find top channels by subscribers and videos count
    top_subscribers = df[['name', 'subscribers']].sort_values(by='subscribers', ascending=False).head(10)
    top_videos = df[['name', 'videos_count']].sort_values(by='videos_count', ascending=False).head(10)

    # Display the results
    st.header("Top Channels by Subscribers")
    st.dataframe(top_subscribers)

    st.header("Top Channels by Video Count")
    st.dataframe(top_videos)

    # Optionally, you can add charts
    st.bar_chart(top_subscribers.set_index("name"))
    st.bar_chart(top_videos.set_index("name"))
else:
    st.info("Please upload a CSV file to see the analysis.")
