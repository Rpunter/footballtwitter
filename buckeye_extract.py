################################################################################
# This file streams twitter data using Twitter Streaming API and tweepy.  The 
# base code for the class defined below come from the tweepy tutorial found on 
# the following website:
#     http://sentdex.com/sentiment-analysisbig-data-and-python-tutorials-algorithmic-trading/how-to-use-the-twitter-api-1-1-to-stream-tweets-in-python/
################################################################################

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

## File directory
nw_dir = 'C:/Users/kavisid/Documents/Northwestern MSPA/Predict 452/Twitter extract/'

## Twitter authentication
CONSUMER_KEY = 'QaGsVUKQXy542NFtWebSw'
CONSUMER_SECRET = 'jCaeabnyna55FTG5pSGeXiJ706SY1aXoTmAKzFu8MA'
ACCESS_TOKEN_KEY = '1432031617-If08klaq6iJclOMNYjIG8X1znPOEpWp82cgLNWf'
ACCESS_TOKEN_SECRET = 'gGad6EgSMBwRjtfEValbtFjTSybqfYDswSEIUYxGkM'

## Create a class to stream Twitter data and save it to a local file
class listener(StreamListener):
    
    def on_data(self, data):
        try:
            #print data
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print tweet
            savethis = str(time.time())+'::'+tweet
            ## Append tweet to existing data file
            saveFile = open(nw_dir+'bulls_20150529.csv','a')
            saveFile.write(savethis)
            ## Put one extra line between each tweet
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            ## Include exception in case streaming/save fails so that the stream
            ## does not close.
            print 'failed ondata,',str(e)
            ## 5 second pause before re-streaming to prevent immediate re-error
            ## and allow for the connection to the stream to reestablish.
            time.sleep(5)
    
    def on_error(self, status):
        ## Print HTTP status if call errors (usually when credentials are wrong)
        print status


## Define and set OAuth credientials
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

## Stream Twitter data using tweepy!!!
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['#nbaplayoffs'])