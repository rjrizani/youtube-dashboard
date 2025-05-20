import googleapiclient.discovery
import pandas as pd
import streamlit as st

DEVELOPER_KEY = st.secrets["youtube"]["youTube-key"]

if not DEVELOPER_KEY:
    raise ValueError("No API key provided. Please set the YOUTUBE_API_KEY environment variable.")

api_service_name = "youtube"
api_version = "v3"

def get_description(videoId="-3QV0vhCeHg"):
    # Get the description from the YouTube video.
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.videos().list(
        part="snippet",
        id=videoId
    )

    response = request.execute()
    # print(response)  # For debugging

    items = response.get('items', [])
    if not items:
        return "No description found or invalid video ID."
    return items[0]['snippet']['description']


desc = get_description()
print(str(desc))