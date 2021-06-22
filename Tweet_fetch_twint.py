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

#Sentiment analysis
import pandas as pd
tweet = twint_to_pd(["tweet"])
type(tweet)

tweet = tweet.to_string(index=False)
type(tweet)

from textblob import TextBlob
b1 = TextBlob(tweet)
print(b1.sentiment)

#Cleaning the data
import re
tweet = re.sub("[^A-Za-z0-9]+"," ",tweet)

#Tokenization
import nltk
from nltk.tokenize import word_tokenize
Tokens = word_tokenize(tweet)
len(Tokens)

#To see Frequency of distinct elements
from nltk.probability import FreqDist
fdist = FreqDist()

for word in Tokens:
    fdist[word] += 1

#Stemming
from nltk.stem import PorterStemmer
ps = PorterStemmer()
Text = []
for w in Tokens:
    Text.append(ps.stem(w))
len(Text)

#Remove Stopwords
import nltk.corpus
stopwords = nltk.corpus.stopwords.words('english')

filtered_sentence = []
for FinalWord in Tokens:
    if FinalWord not in stopwords:
        filtered_sentence.append(FinalWord)  

filtered_sentence
len(filtered_sentence)

#Sentiment Score
#since TextBlob takes only str input, convert the list to string by List Comprehension
filtered_sentence = ' '.join([str(elem) for elem in filtered_sentence])

b2 = TextBlob(filtered_sentence)
print(b2.sentiment)
#Polarity = 0.2778 --> Positive 

from wordcloud import WordCloud
word_cloud = WordCloud(width =2000, height = 2000, background_color='white', stopwords=stopwords, max_words=100, min_font_size=10).generate(filtered_sentence)
import matplotlib.pyplot as plt
plt.figure( figsize=(20,10) )
plt.imshow(word_cloud)



















