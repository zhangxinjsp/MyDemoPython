#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pymysql  # 连接数据库


class MySqlManager:
    cursor = None
    db_connect = None

    def __init__(self):
        print("init sql manager")

    def connect_database(self):
        self.db_connect = pymysql.connect(host='127.0.0.1',  # 连接名称，默认127.0.0.1
                                          user='root',  # 用户名
                                          passwd='12345678',  # 密码
                                          port=3306,  # 端口，默认为3306
                                          db='test',  # 数据库名称
                                          charset='utf8'  # 字符编码
                                          )
        if self.db_connect:
            print("connect success")
        else:
            print("connect failed")
        self.cursor = self.db_connect.cursor()  # 生成游标对象

    def create_table(self, table_name, columns):
        sql = "CREATE TABLE IF NOT EXISTS %s (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT" % table_name

        for column in columns:
            sql += (", " + column + " varchar(255)")
        sql = sql + ")"
        print('create table sql is: ' + sql)
        self.cursor.execute(sql)  # 执行SQL语句

    def insert(self, table, insert_dict):

        keys = ""
        values = ""
        for (key, value) in insert_dict.items():
            keys += key + ", "
            values += "'" + value + "'" + ", "
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, keys[:-2], values[:-2])
        print("insert sql is: " + sql)
        try:
            insert_result = self.cursor.execute(sql)
            print('insert result %d' % insert_result)
            self.db_connect.commit()

            self.cursor.execute('SELECT MAX(id) FROM table_two')
            data = self.cursor.fetchall()  # 通过fetchall方法获得数据
            print(data[0][0])

        except:
            # Rollback in case there is any error
            print('insert error')
            self.db_connect.rollback()


    # cursor.close()  # 关闭游标
    # cursor.close()  # 关闭连接


if __name__ == '__main__':
    manager = MySqlManager()

    manager.connect_database()
    # manager.create_table("table_two", ["column1", "column2"])
    manager.insert("table_two", {"column1": "zhangxin", "column2": "30"})
