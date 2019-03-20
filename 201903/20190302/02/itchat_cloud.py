# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Description: 好友前面词云
@Date: 2019-03-19 15:12:01
'''

import itchat
import re
import os
import jieba
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from wordcloud import WordCloud, ImageColorGenerator

itchat.login()
friends = itchat.get_friends(update=True)[0:]
tList = []

for i in friends:
    signature = i['Signature'].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = re.sub("", signature)
    tList.append(signature)


text = "".join(tList)

wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d, "xiaohuangren.jpg")))
my_wordcloud = WordCloud(background_color='white', max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42,
                         font_path='C:\Windows\Fonts\msyh.ttf').generate(wl_space_split)

image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()

my_wordcloud.to_file(os.path.join(d, "wechat_cloud.png"))
itchat.send_image("wechat_cloud.png", 'filehelper')
