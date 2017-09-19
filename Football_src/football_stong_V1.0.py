#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "DaChao"
# Date: 2017/9/18


import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup
import re

# 图片地址

num = 0
# 发出请求
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

# 说话列表
goal_list = {1: "排名前三哦",
             2: "主队胜率大哦",
             3: "客队有翻盘的可能哦",
             4: "豪赌",
             5: "可赌", }


def minNums(list):
    '''
    胜率最小值
    :param list: 主平客胜率
    :return: 最低胜率，最低胜率索引
    '''
    min_num = min(list)
    min_index = list.index(min_num)
    return min_num, min_index

def algorithm(list):
    '''
    购彩逻辑
    :param list: 每场比赛列表（主队排名、主队、客队、客队排名、主胜率、平胜率、客胜率）
    :return:
    '''
    zhu_rank = int(list[0])
    ke_rank = int(list[3])
    zhu_num = float(list[4])
    ping_num = float(list[5])
    ke_num = float(list[6])

    if zhu_rank < 4 and ke_rank > 4:
        goal = list[1] + "VS" + list[2] + "===>主队" + list[1] +" "+ goal_list[1]
        print("\033[31m%s\033[0m" % (goal))
    elif ke_rank < 4 and zhu_rank > 5:
        goal = list[1] + "VS" + list[2] + "===>客队" + list[2] +" "+ goal_list[1]
        print("\033[32m%s\033[0m" % (goal))
    elif ke_rank - zhu_rank >= 5 and ke_num > zhu_num:
        goal = list[1] + "VS" + list[2] + "===>" + list[1] +" "+ goal_list[2]
        print("\033[33m%s\033[0m" % (goal))
    elif ke_num > zhu_num and ke_rank < zhu_rank:
        goal = list[1] + "VS" + list[2] + "===>" + list[2] +" "+ goal_list[3]
        print("\033[34m%s\033[0m" % (goal))
    else:
        print(goal_list[4])

    # 最小概率都大于1.9，可博
    chance_lists = [zhu_num, ping_num, ke_num]
    min_num, min_index = minNums(chance_lists)

    if min_num > 1.9:
        if min_index == 0:
            print("\033[35m主队 %s %s\033[0m" % (list[1], min_num))
        elif min_index == 2:
            print("\033[35m客队 %s %s\033[0m" % (list[2], min_num))
        else:
            print("\033[35m平局 %s\033[0m" % (min_num))

    return None


def makeMyOpener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


# 顺序：英超8，意甲13，西甲7，德甲9，法甲16
url_list = [{"英超": "http://saishi.caipiao.163.com/8/0000.html"},
            {"意甲": "http://saishi.caipiao.163.com/13/0000.html"},
            {"西甲": "http://saishi.caipiao.163.com/7/0000.html"},
            {"德甲": "http://saishi.caipiao.163.com/9/0000.html"},
            {"法甲": "http://saishi.caipiao.163.com/16/0000.html"}]

for zuqiu_url_dict in url_list:  # .keys/.values 以列表形式返回键值
    league_name = list(zuqiu_url_dict.keys())[0]
    print("\033[5;36m**********%s**********\033[0m" % (league_name))
    oper = makeMyOpener()
    m_request = oper.open(list(zuqiu_url_dict.values())[0], timeout=2)
    # m_request = oper.open("http://saishi.caipiao.163.com/8/0000.html", timeout=2)
    # 获取返回结果
    m_data1 = m_request.read().decode('utf-8')

    soup = BeautifulSoup(m_data1, 'html.parser')
    tr = soup.select('#scoreLive tr')

    # 正则匹配原则
    com = re.compile(
        "\((?P<主队排名>\d+)\)(?P<主队>\D+)-(?P<客队>\D+)\((?P<客队排名>\d+)\)-(?P<主胜>\d+\.\d*)-(?P<平局>\d+\.\d*)-(?P<客胜>\d+\.\d*)\-?")

    for line in tr:
        play_str = ""
        a = line.find_all('td')
        try:
            for i in [1, 3, 5, 6, 7]:
                b = a[i].get_text().strip()
                b = str(b).strip().replace(' ', '').replace('\r\n', '') + "-"
                # print(b, end="")
                play_str += b
            # print("play_str:::::::::::", play_str)
            play_str2 = list(com.findall(play_str)[0])  # 返回列表形式每场比赛数据
            print(play_str2)
            algorithm(play_str2)
            print('')
        except Exception as a:
            pass
