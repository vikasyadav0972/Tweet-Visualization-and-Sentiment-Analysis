import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
# Insert your Twitter API key and secret here
consumer_key = ' '
consumer_secret = ' '
access_token=" "
access_token_secret=" "
# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Create Tweepy API object
api = tweepy.API(auth)
# Define search query and number of tweets to analyze

query = 'USA'
num_tweets = 1000

# Search for tweets containing the query
tweets = tweepy.Cursor(api.search, q=query, lang='en').items(num_tweets)
# Initialize sentiment counters
positive_sentiment = 0
negative_sentiment = 0
neutral_sentiment = 0
# Perform sentiment analysis on each tweet and update counters
for tweet in tweets:
    text = tweet.text
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        positive_sentiment += 1
    elif sentiment < 0:
        negative_sentiment += 1
    else:
        neutral_sentiment += 1
# Calculate percentage of positive, negative, and neutral tweets
total_sentiment = positive_sentiment + negative_sentiment + neutral_sentiment
positive_percent = positive_sentiment / total_sentiment * 100
negative_percent = negative_sentiment / total_sentiment * 100
neutral_percent = neutral_sentiment / total_sentiment * 100
# Print sentiment percentages
print(f"Positive: {positive_percent:.2f}%")
print(f"Negative: {negative_percent:.2f}%")
print(f"Neutral: {neutral_percent:.2f}%")
# Create pie chart of sentiment percentages
labels = ['Positive', 'Negative', 'Neutral']
sizes = [positive_percent, negative_percent, neutral_percent]
colors = ['yellowgreen', 'red', 'blue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()