# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time, random
from multiprocessing import Process, Queue


# 设置一个写入的进程
def writePro(p):
    print('process %s start to write...' % os.getpid())
    for value in ['a', 'b', 'c', 'd']:
        print('put %s to the queue' % value)
        p.put(value)
        time.sleep(random.random())
    return


# 设置一个读取的进程
def readPro(p):
    print('process %s start to read...' % os.getpid())
    while (True):
        value = p.get(True)
        print('read %s from the queue' % value)
    return


if __name__ == '__main__':
    q = Queue()
    wp = Process(target=writePro, args=(q,))
    rp = Process(target=readPro, args=(q,))
    wp.start()
    rp.start()
    wp.join()
    rp.terminate()


"""
process 27857 start to write...
put a to the queue
process 27858 start to read...
read a from the queue
put b to the queue
read b from the queue
put c to the queue
read c from the queue
put d to the queue
read d from the queue

Process finished with exit code 0
"""