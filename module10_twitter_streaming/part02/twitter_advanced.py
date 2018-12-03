"""
Your task today is to complete the functions below, which do some sort of simple information retrieval
from a stream of tweets stored in a file
# More info about the Twitter API at: https://dev.twitter.com/overview/api
"""

import json

from sandobox_module10_text_analysis.part01_lexical_complexity.text_analysis_one import *

def most_followed_user_tweet(output_file):
    """
    This function should print on console and return the tweet in output_file tweeted by the user with most followers,
     the name of the user, and the user's number of followers
     (if the most followed user has tweeted more than once, the oldest tweet should be selected)
    :param output_file:
    :return:
    """
    pass

# extract tweet that hs been retweeted the most

def most_status_changes_user_tweet(output_file):
    """
    This function should print on console and return the tweet in output_file tweeted by the user that has tweeted
    the most since joining twitter.
     the name of the user, and the user's number of followers
     (if the most followed user has tweeted more than once, the oldest tweet should be selected)

    :param output_file:
    :return:
    """
    pass

# evaluate the lexical complexity of your twitter "corpus" using the metrics defined before
# tag and analyse tweets

def lexical_complexity_tweet_stream(output_file, metric, weights):
    """
    This function returns the value of the lexicaly complexity, measured by the metric "metric", of tweets
    contained in output_file

    Note that you will have to import the code tha you have developed in module10 part01 to complete this function

    Suggestion: create a string by concatenating all the tweets stored. Then conevrt this string into
    a nltk "text" that you can pass as a parameter to the metrics defined in module10

    :param output_file: a file containing tracked tweet(s)
    :param metric: a lexical complexity metric (metric 1, 2, or 3, see module 10)
    :param weights: a list containing the weights (parameters) required by the chosen metric (see module 10)
    :return:
    """
    # put the tweets in a string
    pass

if __name__ == '__main__':

    """ UNCOMMENT AS REQUIRED"""

    #most_followed_user_tweet("../part01/test_tweet.json")               # Note the path to the file: .. is used to go up one level in the directory structure

    #most_status_changes_user_tweet("../part01/test_tweet.json")

    #print(lexical_complexity_tweet_stream("../part01/test_tweet.json", 1, [3]))