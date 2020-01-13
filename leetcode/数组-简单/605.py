# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-19 10:09:17
@LastEditTime: 2019-11-19 10:16:04
@Description: 种花问题-简单  https://leetcode-cn.com/problems/can-place-flowers/
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        count, i = 0, 1
        while i < len(flowerbed) - 1:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                count += 1
                i += 2
            else:
                i += 1
        return count >= n
