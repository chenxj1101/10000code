# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-01 14:23:36
@LastEditTime: 2019-11-01 14:34:11
@Description: 杨辉三角-简单  https://leetcode-cn.com/problems/pascals-triangle-ii/
'''

from typing import List

def getRow(rowIndex: int) -> List[int]:
        res = [1]
        for _ in range(rowIndex):
            res = [1] + [res[i-1] + res[i] for i in range(1, len(res))] + [1]
        return res


#-------------------------------------------------------------
def generate2(rowIndex: int) -> List[int]:
    result = []
    for i in range(rowIndex+1):
        now = [1]*(i+1)
        if i >= 2:
            for n in range(1,i):
                now[n] = pre[n-1]+pre[n]
        result += [now]
        pre = now
    return result[-1]

print(generate2(3))