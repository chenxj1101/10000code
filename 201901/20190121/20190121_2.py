# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-21 15:31:43
@LastEditTime: 2019-01-21 15:34:52
@Description: douban250  数据分析
'''

import pymongo
import pandas as pd
import matplotlib


#%%
client = pymongo.MongoClient('127.0.0.1', 27017)
client


#%%
db = client['douban']
db


#%%
db.authenticate('douban', 'chenxj123')


#%%
coll = db['book250']
coll


#%%
list(coll.find({}))


#%%
df = pd.DataFrame(list(coll.find({})))
df


#%%
data = df.drop('_id', axis=1)


#%%
data['score'] = data['mark_num'] / 10000 * data['star']


#%%
data['score']

#%%
data

#%%
data['price'].mean()
#%%
data['price'].max()
#%%
data.describe()
#%%
data.iloc[data['price'].idxmax()]
#%%
data.iloc[data['price'].idxmin()]
#%%
data.sort_values('price').head(10)
#%%
data.sort_values('price', ascending=False).head(10)
#%%
data.sort_values('star', ascending=False).head(10)

#%%
data.sort_values('score', ascending=False).head(10)