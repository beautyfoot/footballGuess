#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "DaChao"
# Date: 2017/7/3

'''
V2.0
利用竞彩平台赔率确认买卖选择
V1.0
其它有影响的因素：
1、多少赔率与比例相搭配
2、多少赔率之外的不在算法之内
3、是否加上权重
4、球队排名与近况
'''
import random

def input_peilv():
    '''
    接收外界赔率
    :return:
    '''
    num1 = input("Please input zhudui num: ")
    num2 = input("Please input pingju num: ")
    num3 = input("Please input kechang num: ")
    return num1,num2,num3

def fenpei():
    '''
    根据赔率分配比例
    :return:
    '''
    num1,num2,num3 = input_peilv()
    z1 = float(num3) / (float(num1) + float(num2) + float(num3)) * 20 #注意赔率大小和胜负可能成反比
    k1 = float(num1) / (float(num1) + float(num2) + float(num3)) * 20
    p1 = 20 - z1 - k1
    return z1,p1,k1

def football():
    '''
    足球竞彩
    :return:
    '''
    z1,p1,k1 = fenpei()
    football_random = random.randint(1,20)
    s2 = z1 + p1
    if football_random <= z1:
        print("主胜")
    elif football_random <= s2 and football_random > z1:
        print("平局")
    elif football_random > s2:
        print("客胜")


def football_start():
    while True:
        football()
        flag = input("Go or Quit(g/q): ").strip()
        if flag == "q":
            break

if __name__ == '__main__':
    fooball_start()







