#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "DaChao"
# Date: 2017/7/6

# import os,sys
#
# res_path = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(res_path)

from Football_src import football_V1
from Football_src import football_V2_1
from Football_src import football_V2_2
from Football_src import basketball


def printer():
    while True:
        res = input('''
        1、权重选择，一次循环
        2、赔率输入，20内一次循环
        3、赔率输入，100内10次循环
        4、篮球赔率选择
        5、退出
        ''')
        if res == '1':
            football_V1.football()
        elif res == "2":
            football_V2_1.football_start()
        elif res == "3":
            football_V2_2.football_start()
        elif res == "4":
            basketball.basketball_start()
        elif res == "5":
            print("EXIT!")
            break
        else:
            print("Continue!")


if __name__ == '__main__':
    printer()
