# let's make our programs compatible with Python 3.0/1/2/3
from __future__ import division, print_function
from future_builtins import ascii, filter, hex, map, oct, zip
from nltk.corpus import PlaintextCorpusReader

import numpy as np  # array operations
import pandas as pd  # pandas for data frame operations
import re

# set maximum number of rows to twenty  
pd.options.display.max_rows = 20

#start process_tweet
def processTweet(tweet):
    # process the tweets
     #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('rt @[^\s]+','',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
    #end
 
#Read the tweets one by one and process it
fp = open('twitter_extract_3.csv', 'r')
line = fp.readline()

## File directory
nw_dir = 'C:/Users/kavisid/Documents/Northwestern MSPA/Predict 452/Twitter extract/'
 
while line:
    processedTweet = processTweet(line)
    print(processedTweet)
    savethis = processedTweet
    ## Append tweet to existing data file
    saveFile = open(nw_dir+'buckeyes_20141207.csv','a')
    saveFile.write(savethis)
     ## Put one extra line between each tweet
    saveFile.write('\n')
    saveFile.close()
    line = fp.readline()
#end loop
fp.close() 

