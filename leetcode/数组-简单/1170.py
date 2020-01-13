# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-23 13:08:49
@LastEditTime : 2019-12-23 13:29:07
@Description: 
'''


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans, queries_count, words_count = [], [], []
        words_count = [word.count(min(word)) for word in words]
        for query in queries:
            c = query.count(min(query))
            ans.append(len([x for x in words_count if c < x]))
        return ans