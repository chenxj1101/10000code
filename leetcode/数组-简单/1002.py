# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-09 15:37:17
@LastEditTime: 2019-12-09 15:39:08
@Description: 查找常用字符-简单  https://leetcode-cn.com/problems/find-common-characters
'''

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return [i for c in set(A[0]) for i in c * min(w.count(c) for w in A)] if A else []
