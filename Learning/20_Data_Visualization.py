#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sqlalchemy import create_engine
import collections


def read_from_db():
    engine_path = 'mysql+pymysql://root:12345678@127.0.0.1/event_trace'
    engine = create_engine(engine_path)
    connect = engine.connect()
    connect.begin()
    df = pd.read_sql_table(table_name='basic_info', con=connect, index_col='id', columns=['fps', 'sdk_version'])

    # df = df.replace(to_replace=np.nan, value='0')
    # df = df.dropna()

    df = df.astype(float)
    print(df)

    dic = collections.Counter(df['sdk_version'])  # 列表必须是 hashable type
    print(dic)
    pd.Series(dic).plot(x='aaa', y='asdf', kind='pie', label='sasw', legend=True,
                        autopct='%1.1f%%', shadow=True)

    plt.show()


def read_from_excel():
    # x 只有dataframe对象时，x可用。横坐标
    # y 同上，纵坐标变量
    # kind 可视化图的种类，如line,hist, bar, barh, pie, kde, scatter
    # figsize 画布尺寸
    # title 标题
    # grid 是否显示格子线条
    # legend 是否显示图例
    # style 图的风格

    path = os.path.join(os.path.expanduser('~'), 'Desktop/data_file.xlsx')

    df = pd.read_excel(path)

    df.plot(x='Month', y='Sun', kind='scatter', grid=True)

    df.plot(x='Month', y=['Rain', 'Tmin'], kind='bar')

    ss = df.plot(x='Month', y=['Tmin', 'Tmax'], kind='line', layout=(2, 1), subplots=True, grid=True, )
    print(type(ss))
    print(ss)

    # df.plot(x='Month', y='Rain', kind='barh')

    # df.plot(y='Rain', kind='pie')

    # plt.ylabel('Relative Cell Amount', fontsize=18)

    plt.show()


def refresh_data():
    plt.ion()

    while True:
        min_table = plt.subplot(2, 1, 1)
        min_table.set_title('min')
        plt.plot(df.Month, df.Tmin, 'r-')

        max_table = plt.subplot(2, 1, 2)
        max_table.set_title('max')
        plt.plot(df.Month, df.Tmax, 'g-')

        plt.pause(0.1)


if __name__ == '__main__':
    print('')
    read_from_db()
    # read_from_excel()
