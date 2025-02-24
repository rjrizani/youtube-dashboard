import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("YouTube Comment Analysis")
st.markdown("""
**CSV File Requirements:**
- **replies**: Number of replies
- **likes**: Number of likes
- **comment_text**: "Text of the comment"


Upload a valid CSV file to view detailed summaries and visualizations below.
 
""")


# File uploader for CSV
uploaded_file_C = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file_C is not None:
    # Load the data from the uploaded CSV file
    df = pd.read_csv(uploaded_file_C)  # Update with your file path
    st.title("Comment Analysis")
    st.subheader("Summary Statistics")
    likes_replies_summary = df[['likes', 'replies']].describe()
    st.write(likes_replies_summary)

    # Top comments by likes
    st.subheader("Top Comments by Likes")
    top_likes = df.nlargest(5, 'likes')[['comment_text', 'likes']]
    st.write(top_likes)

    # Top comments by replies
    st.subheader("Top Comments by Replies")
    top_replies = df.nlargest(5, 'replies')[['comment_text', 'replies']]
    st.write(top_replies)

    # Visualizations
    st.subheader("Distribution of Likes")
    plt.figure(figsize=(10, 5))
    plt.hist(df['likes'], bins=30, color='blue', alpha=0.7)
    plt.title('Distribution of Likes')
    plt.xlabel('Likes')
    plt.ylabel('Frequency')
    st.pyplot(plt)

    plt.figure(figsize=(10, 5))
    plt.hist(df['replies'], bins=30, color='green', alpha=0.7)
    plt.title('Distribution of Replies')
    plt.xlabel('Replies')
    plt.ylabel('Frequency')
    st.pyplot(plt)
else:
    st.info("Please upload a CSV file to see the analysis.")

