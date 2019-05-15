# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-05-15 14:54:26
@Description: 
'''

#%%
text = "I am happy today. I feel sad today."

#%%
from textblob import TextBlob
blob = TextBlob(text)
blob

#%%
blob.sentences

#%%
blob.sentences[0].sentiment

#%%
blob.sentences[1].sentiment

#%%
blob.sentiment

#%%
text2 = "我今天很快乐。我今天很愤怒。"

#%%
from snownlp import SnowNLP
s = SnowNLP(text2)

#%%
for sentence in s.sentences:
    print(sentence)

#%%
s1 = SnowNLP(s.sentences[0])
s1.sentiments

#%%
s2 = SnowNLP(s.sentences[1])
s2.sentiments

#%%
