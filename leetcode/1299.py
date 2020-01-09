# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2020-01-09 14:51:05
@LastEditTime : 2020-01-09 14:51:29
@Description: 将每个元素替换为右侧最大元素-简单  https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side
'''


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * (n - 1) + [-1]
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans