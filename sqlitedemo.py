# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
# try:
#     conn = sqlite3.connect('test.db')
#     try:
#         # 创建一个corsor
#         cursor = conn.cursor()
#         # 执行一条sql语句，创建表
#         cursor.execute('CREATE TABLE user (id varchar(20) PRIMARY KEY , name varchar(20))')
#         # 执行sql语句，插入一条信息
#         cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'keller\')')
#         print('rowcount=', cursor.rowcount)
#     finally:
#         cursor.close()
#     conn.commit()
# finally:
#     conn.close()

# 查询记录
try:
    conn = sqlite3.connect('test.db')
    try:
        cursor = conn.cursor()
        # 执行查询语句
        cursor.execute('SELECT * FROM user WHERE id=?',  '1')
        values = cursor.fetchall()
        print(values)
    finally:
        cursor.close()
finally:
    conn.close()