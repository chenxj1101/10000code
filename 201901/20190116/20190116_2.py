# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-16 13:42:23
@LastEditTime: 2019-01-16 13:57:39
@Description: 一些常用的数学函数 
'''

def find_lcm(num1, num2):
    max = num1 if num1 > num2 else num2
    while(True):
        if (max % num1 == 0) and (max % num2 ==0):
            break
        max += 1
    return max


def find_hcf(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 == num2:
        return num1
    if num1 > num2:
        return find_hcf(num1 - num2, num2)
    return find_hcf(num1, num2 - num1)


def find_max(nums):
    max = nums[0]
    for x in nums:
        if x > max:
            max = x
    print(max)


def find_min(nums):
    min = nums[0]
    for x in nums:
        if x < min:
            min = x
    print(min)

def absval(num):
    if num < 0:
        return -num
    else:
        return num


if __name__ == "__main__":
    print(find_lcm(30, 45))