# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import types
from enum import Enum
import logging
import re
from multiprocessing import Pool
import os, time, random
import pickle
import subprocess
import hashlib

md5 = hashlib.md5()
# md5.update('/Users/mpp/Project/PycharmProjects/py3.6/bin/python /Users/mpp/Project/PycharmProjects/python3demo/demo1.py'.encode('utf-8'))
# print(md5.hexdigest())

md5.update('/Users/mpp/Project/PycharmProjects/py3.6/bin/python'.encode('utf-8'))
md5.update(' /Users/mpp/Project/PycharmProjects/python3demo/demo1.py'.encode('utf-8'))
print('521b7fd1b3756d2a231bcd03f63ca02b')
print(md5.hexdigest())
#验证邮件
# m = re.match(r'[0-9a-zA-Z]{1,5}', '120483084dfj230')
# recompile = re.compile(r'^[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+$')
# m = recompile.match('s.wwww23@gima.com')
# print(m.group())
#贪婪匹配
# m = re.match(r'(\d+)(0*)$', '120300')
# print(m.groups())
# #非贪婪匹配
# m = re.match(r'(\d+?)(0*)$', '120300')
# print(m.groups())

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.baidu.com'])
# print('exit code:', r)


# def long_time_task(name):
#     print('process %s (%s) is running...', (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#     return
#
#
# if __name__ == '__main__':
#     print('Parent process %s :' % (os.getpid()))
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('waiting for all task done....')
#     p.close()
#     p.join()
#     print('all done!')

# print(__name__)

# print('process %s start ...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am childprocess %s and my parent process is %s' % (os.getpid(), os.getppid()))
# else:
#     print('I %s created a child process %s' % (os.getpid(), pid))

# d = dict(name='keller', age=20)
# f = open('test.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f = open('test.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)


# def int2(x):
#     return int(x, base=2)
#
#
# print(int2('1101'))

# print(dir('abc'))

# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def getName(self):
#         return self.__name
#
#     def setName(self, name):
#         if name:
#             self.__name = name
#
#     def printfun(self):
#         print(self.__name, self.__score)


# t = Student('keller', 98)
# t.printfun()
# t.name = 'aoekeller'
# print(t.getName())
# t._Student__name = 'saoekeller'
# print(t.getName())
# t.setName('aoekeller')
# print(t.getName())

# print(Student('keler', 98).getName())
# print(dir(Student('keler', 98)))

# class NumObj():
#     def __init__(self):
#         self.x = 10
#         return
#
# n = NumObj()
# n.age = 32;
# print(n.age)
# def setSome(self, some):
#     self.some = some
#
#
# n.setSome = types.MethodType(setSome, n)
# n.setSome('some')
# print(n.some)
# print(NumObj()()))

# class Screen():
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         if not isinstance(value, int):
#             raise ValueError('数据必须是int型')
#         self.__width = value
#
#
# s = Screen()
# s.width = 100
# print(s.width)
# s.width='s'

# class Dog:
#     def __init__(self, age):
#         self.name = 'dog'
#         self.age = age
#         return
#
#     def run(self):
#         print('%s is running...' % self.age)
#         return
#
#
# class Cat:
#     def run(self):
#         print('cat is running...')
#         return
#
#
# class Monster(Dog, Cat):
#     def __init__(self):
#         Dog.__init__(self, Dog('dog21').age)
#         self.name = 'monster'
#         # Dog.__init__(self,self.name)
#         return
#
#
# m = Monster()
# m.run()
# print(m.name)

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, member.value)

# try:
#     print('try...')
#     print(10/3)
# except ZeroDivisionError as e:
#     print('except:', e)
# else:
#     print('else')
# finally:
#     print('finally')

# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#     finally:
#         print('finally...')
#
# main()

# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
#
# def bar():
#     try:
#         foo('0')
#     except ZeroDivisionError as e:
#         print('ValueError!')
#
#
# bar()
# print('end')

# m = re.search('(?<=abc)def', 'abcdef')
# print(m.group(0))

# with open('test.jpg', 'rb') as f:
# print(len(f.readlines()))
# print(f.read())
# for line in f.readlines():
#     print(line.strip())

# try:
#     f = open('test.jpg', 'rb')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('thumb.jpg', 'wb') as f:
#     with open('test.jpg', 'rb') as f1:
#         f.write(f1.read())

# print(os.uname())
# print(os.path.abspath('.'))
#
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
