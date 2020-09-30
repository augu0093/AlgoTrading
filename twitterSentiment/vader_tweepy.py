"""
This script presents tweets retrieved using tweepy and their sentiment scores as evaluated by Vader.
@augustsemrau
"""

# Libraries
import tweepy

# Scripts
from twitterSentiment.vader import VaderSentiment
from twitterSentiment.tweepy_client import TweepyClient

def main():
    # creating object of TwitterClient Class
    api = TweepyClient()

    # calling function to get tweets
    tweets = api.get_tweets(query='Amazon', count=200)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))

    # percentage of neutral tweets
    print("Neutral tweets percentage: {} %".format(100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)))

    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])


if __name__ == '__main__':

    # Initiating Vader modulse class
    Vader = VaderSentiment()

    # Scoring a sentence to test
    score = Vader.sentiment_analyzer_scores('The phone is cool :)')
    print("Compound score: ", score['compound'])




