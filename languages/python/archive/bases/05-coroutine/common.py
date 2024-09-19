# coding: utf8
""" 
@File: common.py
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

import requests
from uuid import uuid4


def download_images(url):
    image_name = uuid4().__str__() + '.png'
    try:
        response = requests.get(url)
        with open(image_name, 'wb') as file:
            file.write(response.content)
        print('下载完成')
    except Exception as error:
        print(error)
