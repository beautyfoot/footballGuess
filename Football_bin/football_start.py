#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "DaChao"
# Date: 2017/7/6

import os,sys

res_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(res_path)


from Football_conf import football_conf

if __name__ == '__main__':
    football_conf.printer()