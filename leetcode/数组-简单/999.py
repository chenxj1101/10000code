# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-09 15:18:51
@LastEditTime: 2019-12-09 15:25:56
@Description: 车的可用捕获量-简单  https://leetcode-cn.com/problems/available-captures-for-rook
'''


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            if 'R' in board[i]:
                raw = i
                break
        colum = board[raw].index('R')
        
        result = 0

        s = ''.join(board[raw])
        s = s.replace('.','')
        if 'pR' in s:
            result += 1
        if 'Rp' in s:
            result += 1
        s = ''.join(i[colum] for i in board)
        s = s.replace('.','')
        if 'pR' in s:
            result += 1
        if 'Rp' in s:
            result += 1
        return result

