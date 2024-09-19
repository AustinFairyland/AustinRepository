# coding: utf8
""" 
@File: main.py
@Editor: PyCharm
@author: Lionel Johnson
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@datetime: 2023-12-31 00:00:00 UTC+08:00
"""

import os
import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import asyncio

from coroutine import test

if __name__ == '__main__':
    try:
        print(asyncio.run(test()))
    except Exception as error:
        print(error)
