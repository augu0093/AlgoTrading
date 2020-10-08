"""
This script presents tweets retrieved using tweepy and their sentiment scores as evaluated by Vader.
@augustsemrau
"""

# Scripts
from twitterSentiment.vader import VaderSentiment
from twitterSentiment.tweepy_client import TweepyClient


def get_twitter_sentiment():

    # creating object of TwitterClient Class
    api = TweepyClient()
    # Same for Vader class
    vader = VaderSentiment()

    # Calling function to get tweets
    tweets, fetched_tweets = api.get_tweets(mode='search', query='Kamela Harris', count=1000)

    # Calculate mean sentiment
    avg = 0
    for tweet in tweets:
        score = vader.sentiment_analyzer_scores(sentence=tweet)
        print(tweet)
        print(score["compound"])
        print("")
        avg += score["compound"]
    avg /= len(tweets)

    return avg



if __name__ == '__main__':

    average = get_twitter_sentiment()
    print(average)


