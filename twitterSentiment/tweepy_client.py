"""
This script calls tweets using tweepy and delivers them to be sentiment analyzed.
@augustsemrau
"""

# Libraries
import re
import tweepy
import sys
from textblob import TextBlob

# Scripts
from keys.keyTwitter import get_twiiter_api_key, get_twitter_secret_key


class TweepyClient(object):
	"""
	Tweepy clinet class for calling tweets
	"""

	# Initialization with API credentials from external script
	def __init__(self):

		# keys and tokens from the Twitter Dev Console
		api_key = get_twiiter_api_key()
		api_secret = get_twitter_secret_key()

		# attempt authentication
		try:
			# create OAuthHandler object
			self.auth = tweepy.OAuthHandler(api_key, api_secret)

			# create tweepy API object to fetch tweets
			self.api = tweepy.API(self.auth)

		except:
			print("Error: Authentication Failed")
			sys.exit(101)

	def clean_tweet(self, tweet):
		"""
		Utility function to clean tweet text by removing links, special characters using simple regex statements.
		"""

		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\S+)", " ", tweet).split())

	def get_tweets(self, query, count=10):
		"""
		Main function to fetch tweets and parse them using tweepy
		"""

		try:
			# Create empty list for the queried tweets
			tweets = []

			# Call twitter api using tweepy to fetch tweets
			fetched_tweets = self.api.search(q=query, count=count, tweet_mode="extended")

			# parsing tweets one by one
			for tweet in fetched_tweets:

				# if tweet.retweeted_status:
				# 	if tweet.retweeted_status.full_text not in tweets:
				# 		tweets.append(tweet.retweeted_status.full_text)
				# else:
				# 	if tweet.full_text not in tweets:
				# 		tweet = tweet_info.full_text

				# Checking if tweet has retweets, in which case we want to avoid replications
				if tweet.retweet_count > 0:
					if tweet.full_text not in tweets:
						tweets.append(tweet.full_text)
				else:
					tweets.append(tweet.full_text)

			# return parsed tweets
			return tweets, fetched_tweets

		except tweepy.TweepError as e:
			# print error (if any)
			print("Error : " + str(e))



if __name__ == "__main__":

	# Initiating TweepyClient for testing
	TweetsCaller = TweepyClient()

	number_tweets = 10
	# call 10 tweets searching for Apple
	test_tweets, test_fetched_tweets = TweetsCaller.get_tweets(query='Joe Biden', count=number_tweets)
	for i in range(len(test_fetched_tweets)):
		print(i)
		print(test_fetched_tweets[i])
		print("")

	for test_tweet in test_tweets:
		print(test_tweet)
		print("")

