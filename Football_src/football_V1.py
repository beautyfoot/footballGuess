#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "DaChao"
# Date: 2017/7/2


'''
其它有影响的因素：
1、多少赔率与比例相搭配
2、多少赔率之外的不在算法之内
3、是否加上权重
4、球队排名与近况
'''
import random

def print_list():
    print("1、主队优势，实力悬殊（4：1：1）\n"
          "2、主队占优（3：2：1）\n"
          "3、两队均衡（2：2：2）\n"
          "4、客队占优（1：2：3）\n"
          "5、客队优势，实力悬殊（1：1：4）")

def make_lala(content):
    '''
    确认比例
    :param content:
    :return:
    '''
    zhusheng = [1]
    pingju = []
    kesheng = [6]
    content = int(content)
    if content == 1:
        zhusheng.append(2)
        zhusheng.append(3)
        zhusheng.append(4)
        pingju.append(5)
    elif content == 2:
        zhusheng.append(2)
        zhusheng.append(3)
        pingju.append(4)
        pingju.append(5)
    elif content == 3:
        zhusheng.append(2)
        pingju.append(3)
        pingju.append(4)
        kesheng.append(5)
    elif content == 4:
        pingju.append(2)
        pingju.append(3)
        kesheng.append(4)
        kesheng.append(5)
    elif content == 5:
        pingju.append(2)
        kesheng.append(3)
        kesheng.append(4)
        kesheng.append(5)
    return zhusheng,pingju,kesheng

def football():
    '''
    足球竞彩
    :return:
    '''
    print_list()
    choice_footall = input("====> ").strip()
    ret = make_lala(choice_footall)
    football_random = random.randint(1,6)
    if football_random in ret[0]:
        print("主胜")
    elif football_random in ret[1]:
        print("平局")
    elif football_random in ret[2]:
        print("客胜")
