"""
Implementing Vader sentiment analysis for use in twitter sentiment.
@augustsemrau
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class VaderSentiment:
    """Class used for analyzing sentiment in tweets"""
    def __init__(self):
        self.analyser = SentimentIntensityAnalyzer()



    def sentiment_analyzer_scores(self, sentence):
        sentiment_score = self.analyser.polarity_scores(sentence)
        # print("Sentence: '{:->40}' Scores: {}".format(sentence, str(score)))
        return sentiment_score

"""
Testing Vader workings
"""
if __name__ == "__main__":

    # Initialize Vader model class
    Vader = VaderSentiment()

    # Scoring a sentence to test
    score = Vader.sentiment_analyzer_scores("The phone is cool :)")
    print("Compound score: ", score['compound'])










