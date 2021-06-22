# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:39:30 2021

@author: Raghunath B
"""
#Twitter tweet data extraction using twint and Sentiment analysis using TextBlob
#To solve compatibility issues with Notebooks and runtime errors
import nest_asyncio
nest_asyncio.apply()

import twint

# Set up TWINT config
c = twint.Config()

c.Search = "Henry Harvin Education"
# Custom output format
c.Limit = 5000 #Max. tweets to be fetched
c.Since = '2019-06-11'
c.Pandas = True #To get output in Pandas DataFrame
twint.run.Search(c)

#Function to get column names of the DataFrame
def column_names():
    return twint.output.panda.Tweets_df.columns
#Function to get the data in the DataFrame
def twint_to_pd(columns):
    return twint.output.panda.Tweets_df[columns]

#See the column names
column_names()

#Select the desired columns
tweet_df = twint_to_pd(["date", "username", "tweet", "hashtags", "nlikes"])
tweet_df.head(10)

#No. of tweets collected
print(len(tweet_df))

#Save the DataFrame to an excel file
tweet_df.to_excel('D:/Analytics/Internship/tweets.xlsx')

