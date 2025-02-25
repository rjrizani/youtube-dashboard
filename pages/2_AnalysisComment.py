import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

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

# Button to load an example dataset
load_example = st.button("Load Example Dataset")

# Example dataset as a string
example_data_text = """likes,replies,comment_text
10,2,This is a comment.
20,5,Another comment.
5,1,Yet another comment.
30,10,Great comment.
15,3,Informative comment.
"""

# Download button for the example dataset
st.download_button(
    label="Download Example Dataset",
    data=example_data_text,
    file_name="example_dataset.csv",
    mime="text/csv"
)

if uploaded_file_C is not None or load_example:
    if uploaded_file_C is None:
        df = pd.read_csv(io.StringIO(example_data_text))
    else:
        df = pd.read_csv(uploaded_file_C)
    
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

    st.subheader("Distribution of Replies")
    plt.figure(figsize=(10, 5))
    plt.hist(df['replies'], bins=30, color='green', alpha=0.7)
    plt.title('Distribution of Replies')
    plt.xlabel('Replies')
    plt.ylabel('Frequency')
    st.pyplot(plt)
else:
    st.info("Please upload a CSV file, click 'Load Example Dataset', or download the example file above to see the analysis.")

