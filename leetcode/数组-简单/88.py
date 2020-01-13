# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-01 11:01:20
@LastEditTime: 2019-11-01 11:14:46
@Description: 合并两个有序数组-简单  https://leetcode-cn.com/problems/merge-sorted-array/
'''

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    nums1[:] = nums1[:m]
    nums1.extend(nums2[:n])
    nums1[:] = sorted(nums1)


########################################
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    nums1[m:m+n] = nums2
    nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m, n = 3, 3

print(merge(nums1, m, nums2, n))