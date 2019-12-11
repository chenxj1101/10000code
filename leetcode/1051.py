# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-11 10:32:21
@LastEditTime: 2019-12-11 10:32:46
@Description: 高度检查器-检查  https://leetcode-cn.com/problems/height-checker
'''

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1,h2 in zip(heights, sorted(heights)))
