# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-04 10:00:37
@LastEditTime: 2019-12-04 10:01:04
@Description: 装置矩阵-简单  https://leetcode-cn.com/problems/transpose-matrix/
'''


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return zip(*A)