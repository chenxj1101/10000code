# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-29 13:36:29
@LastEditTime: 2019-11-29 13:51:24
@Description:  翻转图像-简单  https://leetcode-cn.com/problems/flipping-an-image
'''

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[j ^ 1 for j in reversed(i)] for i in A]
