import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.analysisMl import sentiment

st.title("Sentiment Analysis of YouTube Comments")
st.markdown("""
**CSV File Requirements:** """)

# File uploader for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.write('---')
    st.write('Sentiment Analysis of Comments')
    st.write(sentiment(df))

    # Example 1: Histogram of compound sentiment scores
    newDf = sentiment(df)
    plt.figure(figsize=(10, 6))
    sns.histplot(newDf['compound'], kde=True)
    plt.title('Distribution of Compound Sentiment Scores')
    plt.xlabel('Compound Score')
    plt.ylabel('Frequency')
    st.pyplot(plt)

    # Example 2: Scatter plot of positive vs. negative sentiment
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='pos', y='neg', data=newDf)
    plt.title('Positive vs. Negative Sentiment')
    plt.xlabel('Positive Sentiment')
    plt.ylabel('Negative Sentiment')
    st.pyplot(plt)

    # Example 3: Boxplot of compound sentiment
    plt.figure(figsize=(10,6))
    sns.boxplot(x='compound', data=newDf)
    plt.title('Boxplot of Compound Sentiment')
    st.pyplot(plt)

    # Example 4: Correlation matrix heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(newDf[['neg', 'neu', 'pos', 'compound']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Sentiment Scores')
    st.pyplot(plt)
else:
    st.write('Upload a CSV file to get started')



