"""
This script presents tweets retrieved using tweepy and their sentiment scores as evaluated by Vader.
@augustsemrau
"""

# Libaries
import tweepy

# Scripts
from twitterSentiment.vader import VaderSentiment
from keys.keyTwitter import get_twiiter_api_key, get_twitter_bearer_token, get_twitter_secret_key






if __name__ == '__main__':

    # Initiating Vader modulse class
    Vader = VaderSentiment()

    # Scoring a sentence to test
    score = Vader.sentiment_analyzer_scores('The phone is cool :)')
    print("Compound score: ", score['compound'])




