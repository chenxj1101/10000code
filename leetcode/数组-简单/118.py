# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-01 13:39:41
@LastEditTime: 2019-11-01 14:32:29
@Description: 杨辉三角-简单  https://leetcode-cn.com/problems/pascals-triangle/
'''

from typing import List

def generate(numRows: int) -> List[List[int]]:
    res = [1]
    for _ in range(numRows):
        yield res
        res = [1] + [res[i-1] + res[i] for i in range(1, len(res))] + [1]


#-------------------------------------------------------------
def generate(self, numRows: int) -> List[List[int]]:
    result = []
    for i in range(numRows):
        now = [1]*(i+1)
        if i >= 2:
            for n in range(1,i):
                now[n] = pre[n-1]+pre[n]
        result += [now]
        pre = now
    return result