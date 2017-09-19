#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "DaChao"
# Date: 2017/7/3

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
    # num1,num2,num3 = 1.82,3.30,3.62
    z1 = float(num3) / (float(num1) + float(num2) + float(num3)) * 100
    k1 = float(num1) / (float(num1) + float(num2) + float(num3)) * 100
    p1 = 100 - z1 - k1
    # print("\033[44m====\033[0m",z1,p1,k1)
    return z1,p1,k1,float(num1),float(num2),float(num3)

def football():
    '''
    足球竞彩
    :return:
    '''
    z1,p1,k1,num1,num2,num3 = fenpei()
    s2 = z1 + p1
    num_zhu = 0
    num_ping = 0
    num_ke = 0
    for i in range(9):
        football_random = random.randint(1,100)
        # print("\033[42m====\033[0m",football_random)
        if football_random <= z1:
            num_zhu += 1
        elif football_random <= s2 and football_random > z1:
            num_ping += 1
        elif football_random > s2:
            num_ke += 1
    # print(num_zhu,num_ping,num_ke)
    num_zhu = num_zhu / num3
    num_ping = num_ping / num2
    num_ke = num_ke / num1
    # print(num_zhu,num_ping,num_ke)
    flag = max(max(num_zhu,num_ping),num_ke)
    # print(flag)
    if flag == num_zhu:
        print("主胜")
    elif flag == num_ping:
        print("平局")
    elif flag == num_ke:
        print("客胜")


def football_start():
    while True:
        try:
            football()
        except Exception:
            print("input err!")
        flag = input("Go or Quit(g/q): ").strip()
        if flag == "q":
            break

if __name__ == '__main__':
    football_start()
