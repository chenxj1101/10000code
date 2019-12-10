# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-10 14:08:03
@LastEditTime: 2019-12-10 14:08:26
@Description: 将数组分成和相等的三个部分-简单  https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
'''


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        target = sum(A)//3
        count, s = 0,0
        for i in A:
            s += i
            if s == target:
                count += 1
                s = 0
        return count == 3