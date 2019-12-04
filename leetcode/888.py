# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-04 10:15:00
@LastEditTime: 2019-12-04 10:15:32
@Description: 公平的糖果交换-简单  https://leetcode-cn.com/problems/fair-candy-swap/
'''


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for num in A:
            if num + (Sb-Sa)/2 in setB:
                return [num, num+(Sb-Sa)//2]