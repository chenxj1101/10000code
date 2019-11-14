# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-14 10:24:07
@LastEditTime: 2019-11-14 10:49:17
@Description: 找到所有数组中消失的数字-简单  https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a=set(list(range(1,len(nums)+1)))
        for i in nums:
            a.discard(i)
        return a


#-----------------------------------------------------------------

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))