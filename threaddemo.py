# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    for n in range(5):
        print('thread %s >>> %s' % (threading.current_thread().name, n))
    print('thread %s ended' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='loopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)

"""
输出
thread MainThread is running...
thread loopThread is running...
thread loopThread >>> 0
thread loopThread >>> 1
thread loopThread >>> 2
thread loopThread >>> 3
thread loopThread >>> 4
thread loopThread ended
thread MainThread ended
"""