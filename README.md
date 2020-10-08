# AlgoTrading
Algorithmic-based trading summer project.
By augustsemrau.

## Goal
The system seeks to be profitable.  

Approaches to implementing this task are described in light detail below.  

### Data Source - IEX
Various API's for attaining stock prices and related data excist, IEX seems to be the best.


### Order Integration - Saxo Bank
Using Saxo Bank OpenAPI, orders can be placed directly via the API.
Light description follows.

## Twitter Sentiment Analysis
I am trying to use the sentiment connected with different companies on twitter
to see if it correlates with their stock price.  
In order to do this, I am using the following modules:  

- Tweepy is the client used for retrieving tweets.

- Vader is a sentiment analyzer tuned specifically for social media.
We use it's standardises compound score, ranging from -1 to 1, negative values being negative, positive is positive. 

- NLTK  sdsdsdsd.


## Scripts


1. **tweepy_class** contains the class responsible for calling tweets for sentiment analysis.
2. **vader.py** contains the class that carries out the sentiment analysis.
3. **vader_tweepy** carries out tweet sentiment analysis and produces statistical 
values used for correlating with stock prices.
4. 


## Strategy
TBA

Primary trading strategy is a mix of strategies, based on following articles:  

'Only Take a Trade If It Passes This 5-Step Test'
https://www.investopedia.com/articles/active-trading/090415/only-take-trade-if-it-passes-5step-test.asp  

'10 Day Trading Strategies for Beginners'
https://www.investopedia.com/articles/trading/06/daytradingretail.asp



## Future Strategy Ideas
- NLP from twitter
