import googleapiclient.discovery
import pandas as pd
import streamlit as st

#import os
#from pathlib import Path
#from dotenv import load_dotenv

#env_path = Path('C:/Users/rjriz/freelance') / '.env'
#load_dotenv(dotenv_path=env_path)

#DEVELOPER_KEY = os.getenv("youTube-key")
DEVELOPER_KEY = st.secrets["youtube"]["youTube-key"]

if not DEVELOPER_KEY:
    raise ValueError("No API key provided. Please set the YOUTUBE_API_KEY environment variable.")

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = DEVELOPER_KEY   

def get_comments(videoId="-3QV0vhCeHg"):
    # Get the comments from the YouTube video.
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=videoId,
        maxResults=100
    )

    comments = []

    # Execute the request.
    response = request.execute()


    # print(response)

    # Get the comments from the response.
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        public = item['snippet']['isPublic']
        comments.append([
            comment['authorDisplayName'],
            comment['publishedAt'],
            comment['likeCount'],
            comment['textOriginal'],
            public
        ])

    while (1 == 1):
        try:
            nextPageToken = response['nextPageToken']
        except KeyError:
            break

        nextPageToken = response['nextPageToken']
        # Create a new request object with the next page token.
        nextRequest = youtube.commentThreads().list(part="snippet", videoId="-GJgqIJsTME", maxResults=100, pageToken=nextPageToken)
        # Execute the next request.
        response = nextRequest.execute()
        # Get the comments from the next response.
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            public = item['snippet']['isPublic']
            comments.append([
                comment['authorDisplayName'],
                comment['publishedAt'],
                comment['likeCount'],
                comment['textOriginal'],
                public
            ])

    df = pd.DataFrame(comments, columns=['author', 'updated_at', 'like_count', 'text','public'])
    return df





