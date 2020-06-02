#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql  # 连接数据库

# pip show PyMySQL
# 192.168.0.197
conn = pymysql.connect(host='127.0.0.1',  # 连接名称，默认127.0.0.1
                       user='root',  # 用户名
                       passwd='12345678',  # 密码
                       port=3306,  # 端口，默认为3306
                       db='event_trace',  # 数据库名称
                       charset='utf8',  # 字符编码
                       )

cur = conn.cursor()  # 生成游标对象

sql = "INSERT INTO table_one (name, age, birthday) VALUES ('hao1', 30, '2010-10-10')"
cur.execute(sql)  # 执行SQL语句

sql = "select * from `table_one` "  # SQL语句
cur.execute(sql)  # 执行SQL语句
data = cur.fetchall()  # 通过fetchall方法获得数据
for i in data:  # 打印输出前2条数据
    print(i)

cur.close()  # 关闭游标
conn.close()  # 关闭连接

if __name__ == '__main__':
    # generated_document('0.0.1', '0.0.3')
    print('asdfasdf')
