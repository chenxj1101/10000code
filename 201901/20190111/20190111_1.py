# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-11 15:38:04
@LastEditTime: 2019-01-14 15:26:41
@Description: 暴力破解加密rar, 多进程，多进程+多线程
'''

import random
import time
import queue
import threading
from unrar import rarfile
from multiprocessing.pool import Pool
from functools import partial


def generate_psd():
    code_list = []
    for i in range(10):
        code_list.append(str(i))
    for i in range(65, 91):
        code_list.append(chr(i))
    for i in range(97, 123):
        code_list.append(chr(i))
    
    myslice = random.sample(code_list, 6)
    passwd = ''.join(myslice)
    return passwd


def generate_dict(passwd):
    with open(passwd, 'a', encoding='utf-8') as f:
        for i in range(50000):
            code = generate_psd()
            print(code, file=f)


def un_encrypted_rar(rar, pwd):
    fp = rarfile.RarFile(rar)
    try:
        fp.extractall(path='./', pwd=pwd)
        print(f'{pwd} is the true passwd' )
        fp._close
        return True

    except:
        return False

if __name__ == "__main__":
    passwd = './passwd.txt'
    rar = './201812.rar'
    ts = time.time()
    f = open(passwd)
    pwds = [pwd.strip() for pwd in f.readlines()]

    p = Pool(processes=5)

    # 多进程+多线程写法  返回值为True则结束所有子进程，117s
    result = queue.Queue()

    def pool_th():
        for pwd in pwds:
            try:
                result.put(p.apply_async(un_encrypted_rar, args=(rar, pwd)))
            except:
                break

    def result_th():
        while 1:
            a = result.get().get()
            if a:
                p.terminate()
                break
    
    '''
    利用多线程，同时运行pool函数创建执行子进程，以及运行获取子进程返回值函数
    '''
    t1 = threading.Thread(target=pool_th)
    t2 = threading.Thread(target=result_th)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


    p.join()

    # 多进程写法  250s
    # partial_un_encrypted_rar = partial(un_encrypted_rar, rar)
    # p.map(partial_un_encrypted_rar, pwds)

    # 单进程写法 1000s
    # for pwd in pwds:
    #     print(pwd)
    #     un_encrypted_rar(rar, pwd)
    print(f'cost time is {time.time()-ts:.2f}s')
