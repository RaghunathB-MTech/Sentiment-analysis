#Data cleaning for sentiment analysis

#Importing libraries
import re
import pandas as pd
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
import spacy
import numpy as np

#Load the dataset
df = pd.read_csv('D:/Analytics/Internship/HH_FINAL.csv',encoding='utf-8',errors='ignore')
#UnicodeDecodeError arised.

#To solve the error
file = 'D:/Analytics/Internship/HH_FINAL.csv'
import chardet
with open(file, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
result

df = pd.read_csv(file,encoding='ISO-8859-1')
df

#Check for missing rows and handling them
df.isnull().sum() #2 rows have missing values
df.dropna(subset=['comments'],inplace=True)

#Initialize Spacy ‘en’ model
nlp = spacy.load("en_core_web_sm")

#Make text lowercase
df['new_reviews'] = df['comments'].apply(lambda x: " ".join(x.lower() for x in x.split()))

#Remove punctuation
df['new_reviews'] = df['new_reviews'].str.replace('[^\w\s]','')

#Remove emojis
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags 
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)
df['new_reviews'] = df['new_reviews'].apply(lambda x: remove_emoji(x))

#Remove stopwords
stop = stopwords.words('english')
df['new_reviews'] = df['new_reviews'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

#Lemmatization
def space(comment):
    doc = nlp(comment)
    return " ".join([token.lemma_ for token in doc])
df['new_reviews']= df['new_reviews'].apply(space)

#Write to a csv file
df.to_csv('D:/Analytics/Internship/HH_CLEAN.csv')







