# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-10-31 13:59:57
@LastEditTime: 2019-10-31 14:07:21
@Description: 删除排序数组中的重复项-简单  https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow, nums[slow] = slow+1, nums[fast]
            
        return slow + 1