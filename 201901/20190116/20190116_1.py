# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-16 10:33:44
@LastEditTime: 2019-01-16 10:37:56
@Description: lru_cache装饰器的使用
'''

import time
from functools import lru_cache

def clock(func):
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:.8f}s] {name}({arg_str}) -> {result}')
        return result
    return clocked

@lru_cache(128)
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == "__main__":
    print(fibonacci(10))
    t0 = time.time()
    for i in range(100):
        print(time.time() - t0)