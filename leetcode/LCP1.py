# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-10-31 13:58:32
@LastEditTime: 2019-10-31 14:06:48
@Description: 猜数字-简单  https://leetcode-cn.com/problems/guess-numbers/
'''

class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
            return sum(guess[i]==answer[i] for i in range(len(guess)))