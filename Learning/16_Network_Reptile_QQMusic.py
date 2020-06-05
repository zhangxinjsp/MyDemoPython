#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'geci'

sheet['A1'] = '歌曲名'  # 加表头，给A1单元格赋值
sheet['B1'] = '所属专辑'  # 加表头，给B1单元格赋值
sheet['C1'] = '播放时长'  # 加表头，给C1单元格赋值
sheet['D1'] = '播放链接'  # 加表头，给D1单元格赋值
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):

    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }

    res_music = requests.get(url, params=params)
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    for music in list_music:
        # print(music['name'])
        # print('所属专辑：' + music['album']['name'])
        # print('播放时长：' + str(music['interval']) + '秒')
        # print('播放链接：https://y.qq.com/n/yqq/song/' + music['file']['media_mid'] + '.html\n\n')

        name = music['name']
        album = music['album']['name']
        time = str(music['interval'])
        link = 'https://y.qq.com/n/yqq/song/' + music['file']['media_mid'] + '.html\n\n'

        row = [name, album, time, link]
        sheet.append(row)
wb.save('/Users/zhangxin/Desktop/zhoujielun1.xlsx')
