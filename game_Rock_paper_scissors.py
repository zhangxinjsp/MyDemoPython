# coding=utf-8

import random

while True:
    s = int(random.randint(1, 3))
    if s == 1:
        ind = "石头"
    elif s == 2:
        ind = "剪刀"
    elif s == 3:
        ind = "布"
    m = input("请输入石头，剪刀，布， 输入end结束：")
    blist = ["石头", "剪刀", "布"]
    if m == "end":
        print("结束游戏")
        break
    elif m not in blist:
        print("输入错误：")
    elif m == ind:
        print("平局")
    elif (m == "石头" and ind == "剪刀") or (m == "剪刀" and ind == "布") or (m == "布" and ind == "石头"):
        print("电脑出：" + ind + "你赢了")
    elif (m == "剪刀" and ind == "石头") or (m == "布" and ind == "剪刀") or (m == "石头" and ind == "布"):
        print("电脑出：" + ind + "你输了")
