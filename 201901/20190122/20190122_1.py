# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-22 13:38:42
@LastEditTime: 2019-01-23 11:08:10
@Description: Async/Await 入门实例
'''

import random
import asyncio

class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos


all_potatos = Potato.make(5)


async def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break


async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))


async def buy_potatos():
    bucket = []
    async for p in take_potatos(50):
        bucket.append(p)
        print(f'Got potato {id(p)}...')


async def buy_tomatos():
    bucket = []
    async for p in take_potatos(50):
        bucket.append(p)
        print(f'Got tomato {id(p)}...')



def main():
    loop = asyncio.get_event_loop()
    # res = loop.run_until_complete(buy_potatos())
    res = loop.run_until_complete(asyncio.wait([buy_potatos(), buy_tomatos()]))
    loop.close()


main()