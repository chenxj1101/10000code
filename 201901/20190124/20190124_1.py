# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-24 09:39:40
@LastEditTime: 2019-01-24 13:45:53
@Description: 常用技巧
'''

# 1.使用元组改善分支代码

import bisect
import time


def from_now0(ts):
    """
    接收一个过去的时间戳，返回距离当前时间的相对时间文字描述
    """
    now = time.time()
    seconds_delta = int(now - ts)
    if seconds_delta < 1:
        return "less than 1 second ago"
    elif seconds_delta < 60:
        return f"{seconds_delta} seconds ago"
    elif seconds_delta < 3600:
        return f"{seconds_delta // 60} minutes ago"
    elif seconds_delta < 3600 * 24:
        return f"{seconds_delta // 3600} hours ago"
    else:
        return f"{seconds_delta // (3600 * 24)} days ago"



BREAKPOINTS = (1, 60, 3600, 3600*24)
TMPLS = (
    (1, "less than 1 second ago"),
    (1, "{units} seconds ago"),
    (60, "{units} minutes ago"),
    (3600, "{units} hours ago"),
    (3600*24, "{units} days ago"),
)

def from_now(ts):
    seconds_delta = int(time.time() - ts)
    unit, tmpl = TMPLS[bisect.bisect(BREAKPOINTS, seconds_delta)]
    return tmpl.format(units = seconds_delta // unit)


now = time.time()

print(from_now(now))
print(from_now(now - 24))
print(from_now(now - 600))
print(from_now(now - 7500))
print(from_now(now - 87500))


# 动态解包 可用于字典合并

user = {**{'name': 'piglei'}, **{'movies': ["Fight Club"]}}
print(user)

# 使用next
numbers = [3, 7, 8, 2, 21]
print(next(i for i in numbers if i % 2 == 0))

# 最好不用“获取许可”，也无需“要求原谅”
# AF: Ask for Forgiveness
# 要做就做，如果抛出异常了，再处理异常
# 社区偏爱方式，抛出异常是轻量操作，性能更好，不用每次循环时都做一次额外的检查

def conter_af(l):
    result = {}
    for key in l:
        try:
            result[key] += 1
        except KeyError:
            result[key] = 1
    return result

# AP: Ask for Permission
# 做之前，先问问能不能做，可以做再做
def counter_ap(l):
    result = {}
    for key in l:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result

## 最好的方式

from collections import defaultdict

def counter_by_collectons(l):
    result = defaultdict(int)
    for key in l:
        result[key] += 1
    return result