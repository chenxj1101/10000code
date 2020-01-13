# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-22 14:53:18
@LastEditTime: 2019-11-22 14:56:24
@Description: 1比特与2比特字符-简单  https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/
'''


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if i == len(bits) - 1:
                return True
            if bits[i] == 1:
                i += 1
            i += 1
        return False