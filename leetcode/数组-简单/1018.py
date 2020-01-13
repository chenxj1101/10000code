# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-10 14:23:21
@LastEditTime: 2019-12-10 14:23:46
@Description: 可被 5 整除的二进制前缀-简单  https://leetcode-cn.com/problems/binary-prefix-divisible-by-5
'''


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        s = 0
        res = []
        for n in A:
            s = s*2 + n
            res.append(s % 5 == 0)
        return res