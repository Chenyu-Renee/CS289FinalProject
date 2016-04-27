#import all the packages that needed

import json
import os
import itertools
import numpy as np
import nltk
from nltk.corpus import stopwords
from collections import Counter
import simplejson

#change directory(This needs to be edited)
os.chdir('/Users/riverzhu/Downloads/yelp_training_set')

data=[]
with open('yelp_training_set_review.json') as f:
    for line in f:
        data.append(json.loads(line))

#load original data

def clean_total_words(data):
    all_text=list()
    for i in range(len(data)):
        all_text.append(data[i]['text'])
    words=list()
    for i in range(len(all_text)):
        words.append(nltk.word_tokenize(all_text[i]))
    wordss= list(itertools.chain.from_iterable(words))
    word_after_clean=list()
    for i in range(len(words)):
        wordss[i]=wordss[i].lower()
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    for i in range(len(wordss)):
        if wordss[i] not in stop_words:
            word_after_clean.append(wordss[i])
    word_clean=list()
    for i in range(len(word_after_clean)):
        if word_after_clean[i].isalpha()==True:
            word_clean.append(word_after_clean[i])
    word_clea=list()
    for i in range(len(word_clean)):
        word_clea.append(word_clean[i].lower())
    stop_words = set(stopwords.words('english'))
    word_c=list()
    for i in range(len(word_clea)):
        if word_clea[i] not in stop_words:
            word_c.append(word_clea[i])
    return(word_c)

def select_most_k(k,wor):
    cou=Counter(wor)
    return dict(cou.most_common(k))

data2=list()
for i in range(len(data)):
    data2.append(data[i]['text'])
data3=list()
for i in range(len(data2)):
    data3.append(list())


for i in range(len(data2)):
    for j in range(len(data2[i].split())):
        data3[i].append(data2[i].split()[j].lower())

os.chdir('/Users/riverzhu/Downloads/yelp_test_set')
data_test=list()
with open('yelp_test_set_review.json') as f:
    for line in f:
        data_test.append(json.loads(line))
        
data_test2=list()
for i in range(len(data_test)):
    data_test2.append(data_test[i]['text'])
data_test3=list()
for i in range(len(data_test2)):
    data_test3.append(list())


for i in range(len(data_test2)):
    for j in range(len(data_test2[i].split())):
        data_test3[i].append(data_test2[i].split()[j].lower())

def construct_matrix(df,dat):
    mat=np.zeros((len(dat),len(df)))
    h=list(df.keys())
    for i in range(len(dat)):
        for j in range(len(h)):
            mat[i][j]=dat[i].count(h[j])
    return mat


#sample code below:
#k=1000
#worr=clean_total_words(data)
#df=select_most_k(k,worr)
#train_word_matrix=construct_matrix(df,data3)
#test_word_matrix=construct_matrix(df,data_test3)