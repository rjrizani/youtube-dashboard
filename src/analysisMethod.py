import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from src.extraction import get_comments
import pandas as pd

def sentiment(df):  
    # Initialize the VADER sentiment intensity analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Get the comments from the DataFrame
    comments = df['text']

    # Create a list to store the data
    data_list = []

    # Analyze the sentiment of each comment
    for comment in comments:
        sentiment = analyzer.polarity_scores(comment)
        # Create a dictionary for each row
        row_data = {
            'comment': comment,
            'neg': sentiment['neg'],
            'neu': sentiment['neu'],
            'pos': sentiment['pos'],
            'compound': sentiment['compound']
        }
        data_list.append(row_data)

    # Create the DataFrame from the list of dictionaries
    newDf = pd.DataFrame(data_list)
    return newDf

    