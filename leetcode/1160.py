# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-23 10:33:30
@LastEditTime: 2019-12-23 10:41:11
@Description: 拼写单词-简单  https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/
'''


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        flag = 0
        for w in words:
            for i in w:
                if w.count(i) <= chars.count(i):
                    flag = 1
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                ans += len(w)
        return ans