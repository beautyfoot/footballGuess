#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "DaChao"
# Date: 2017/9/7


import random

def input_peilv():
    '''
    接收外界赔率
    :return:
    '''
    num1 = input("Please input zhudui num: ")
    num2 = input("Please input kechang num: ")
    return num1, num2


def fenpei():
    '''
    根据赔率分配比例
    :return:
    '''
    num1, num2 = input_peilv()
    # num1,num2,num3 = 1.82,3.30,3.62
    z1 = float(num2) / (float(num1) + float(num2)) * 100
    k1 = 100 - z1
    # print("\033[44m====\033[0m",z1,p1,k1)
    return z1, k1, float(num1), float(num2)


def basketball():
    '''
    足球竞彩
    :return:
    '''
    z1, k1, num1, num2 = fenpei()
    num_zhu = 0
    for i in range(9):
        football_random = random.randint(1,100)
        # print("\033[42m====\033[0m",football_random)
        if football_random <= z1:
            num_zhu += 1
    if num_zhu >= 5:
        print("主胜")
    else:
        print("客胜")


def basketball_start():
    while True:
        try:
            basketball()
        except Exception:
            print("input err!")
        flag = input("Go or Quit(g/q): ").strip()
        if flag == "q":
            break

if __name__ == '__main__':
    basketball_start()

