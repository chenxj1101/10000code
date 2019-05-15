# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-05-14 13:30:49
@Description: 
'''

#%%
import pandas as pd

#%%
df = pd.read_csv('201905\learn1\loans.csv')

#%%
df.head()

#%%
df.shape

#%%
X = df.drop('safe_loans', axis=1)
y = df.safe_loans

#%%
X.shape

#%%
y.shape

#%%
X.head()

#%%
y.head()

#%%
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
d = defaultdict(LabelEncoder)
X_trans = X.apply(lambda x: d[x.name].fit_transform(x))
X_trans.head()

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_trans, y, random_state=1)

#%%
X_train.shape

#%%
y_train.shape

#%%
X_test.shape

#%%
from sklearn import tree
clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(X_train, y_train)

#%%
test_rec = X_test.iloc[1,:]
clf.predict([test_rec])

#%%
y_test.iloc[1]

#%%
from sklearn.metrics import accuracy_score
accuracy_score(y_test, clf.predict(X_test))

#%%
with open('201905\learn1\safe-loans.dot', 'w') as f:
    f = tree.export_graphviz(clf,
                             out_file=f,
                             max_depth=3,
                             impurity=True,
                             feature_names=list(X_train),
                             class_names=['not safe', 'safe'],
                             rounded=True,
                             filled=True)

from subprocess import check_call
check_call(['dot', '-Tpng', '201905\learn1\safe-loans.dot', '-o', '201905\learn1\safe-loans.png'])

#%%
from IPython.display import Image as PImage
from PIL import Image, ImageDraw, ImageFont
img = Image.open('201905\learn1\safe-loans.png')
draw = ImageDraw.Draw(img)
img.save('output.png')


#%%
