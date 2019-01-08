# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-08 14:56:22
@LastEditTime: 2019-01-08 15:15:23
@Description: bogo sort 猴子排序
'''

import random


def bogosort(collection):
    """
    Pure implementation of the bogosort algorithm in Python
    :param collection: some mutable orderd collection with hterogeneous
    comparable items inside
    :return: the sam collection ordered by ascending
    Examples:
    >>> bogosort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bogosort([])
    []
    >>> bogosort([-2, -5, -45])
    [-45, -5, -2]
    """

    def isSorted(collection):
        if len(collection) < 2:
            return True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i +1]:
                return False
        return True

    while not isSorted(collection):
        random.shuffle(collection)
    return collection

if __name__ == "__main__":
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(bogosort(unsorted))
