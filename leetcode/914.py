# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-05 10:16:15
@LastEditTime: 2019-12-05 10:20:23
@Description: 卡牌分组-简单  https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/
'''

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from fractions import gcd
        from functools import reduce
        from collections import Counter
        val = Counter(deck).values()
        return reduce(gcd, val) >= 2
