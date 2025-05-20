import googleapiclient.discovery
import google.generativeai as genai # Import the Gemini library
import pandas as pd
import streamlit as st
import os

# --- YouTube API Configuration ---
YOUTUBE_DEVELOPER_KEY = st.secrets.get("youtube", {}).get("youTube-key")
if not YOUTUBE_DEVELOPER_KEY:
  
    YOUTUBE_DEVELOPER_KEY = os.environ.get("YOUTUBE_API_KEY") 
if not YOUTUBE_DEVELOPER_KEY:
    raise ValueError("No YouTube API key provided. Please set it in st.secrets or as YOUTUBE_API_KEY environment variable.")

youtube_api_service_name = "youtube"
youtube_api_version = "v3"

# --- Gemini API Configuration ---
GEMINI_API_KEY = st.secrets.get("gemini", {}).get("apiKey")
if not GEMINI_API_KEY:
    # Fallback for local development
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("No Gemini API key provided. Please set it in st.secrets or as GEMINI_API_KEY environment variable.")

genai.configure(api_key=GEMINI_API_KEY)

# --- YouTube Function ---
def get_youtube_description(videoId="-3QV0vhCeHg"):
    """Gets the description from a YouTube video."""
    try:
        youtube = googleapiclient.discovery.build(
            youtube_api_service_name, youtube_api_version, developerKey=YOUTUBE_DEVELOPER_KEY)

        request = youtube.videos().list(
            part="snippet",
            id=videoId
        )
        response = request.execute()
        items = response.get('items', [])
        if not items:
            return "No description found or invalid video ID."
        return items[0]['snippet']['description']
    except Exception as e:
        return f"Error fetching YouTube description: {e}"

# --- Gemini Function ---
def find_sponsors_with_gemini(description_text):
    """Uses Gemini to find sponsors in the provided text."""
    if not description_text or "No description found" in description_text or "Error fetching" in description_text:
        return "Cannot analyze an empty or error-laden description."

    model = genai.GenerativeModel('gemini-1.5-flash-latest') # Or 'gemini-pro' / 'gemini-1.0-pro'
                                                   # 'gemini-1.5-flash' is fast and capable for this
    
    prompt = f"""
    Analyze the following YouTube video description to identify any sponsors or sponsored segments.
    Sponsors are often companies or brands that have paid for a mention, a product placement, or a dedicated segment in the video.
    Look for phrases like "sponsored by", "thanks to our sponsor", "this video is brought to you by", "check out [brand]", affiliate links (though distinguish from direct sponsorships if possible), or dedicated sections talking about a product/service.

    If you find any potential sponsors, list their names.
    If you find multiple, list them all.
    If you are unsure, state that you are unsure but mention the potential candidates.
    If no sponsors are clearly identifiable, state "No clear sponsors identified."

    Video Description:
    ---
    {description_text}
    ---

    Identified Sponsors:
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error calling Gemini API: {e}"

# --- Main Execution ---
if __name__ == "__main__":
    st.title("YouTube Sponsor Finder")

    video_id_input = st.text_input("Enter YouTube Video ID:", value="-3QV0vhCeHg") # Example: Marques Brownlee - Rewind
                                                                             # For a video with sponsors, try:  (Linus Tech Tips)
                                                                             # or https://www.youtube.com/watch?v=NDsO1LT_0lw (MrBeast)

    if st.button("Analyze Video"):
        if not video_id_input:
            st.warning("Please enter a Video ID.")
        else:
            with st.spinner(f"Fetching description for video ID: {video_id_input}..."):
                description = get_youtube_description(videoId=video_id_input)
            
            st.subheader("Video Description:")
            if "Error fetching" in description or "No description found" in description:
                st.error(description)
            else:
                st.text_area("Description", description, height=200)

                with st.spinner("Asking Gemini to find sponsors..."):
                    sponsor_analysis = find_sponsors_with_gemini(description)
                
                st.subheader("Sponsor Analysis (from Gemini):")
                st.markdown(sponsor_analysis)

    