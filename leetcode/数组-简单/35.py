# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-10-31 14:03:12
@LastEditTime: 2019-10-31 14:04:05
@Description: 搜索插入位置-简单  https://leetcode-cn.com/problems/search-insert-position/
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([i for i in nums if i < target])