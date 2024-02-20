# coding: utf
"""
@ File: __main.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Linux Ubuntu .. Kernel ..--generic 
@ CreatedTime: //
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import requests, time
from lxml import etree

"""
    url:给定的url
    save_file_name:为url存储文件
"""


def Redirect(url):
    try:
        res = requests.get(url, timeout=1)
        url = res.url
    except Exception as e:
        print("", e)
        time.sleep()
    return url


def requests_for_url(url, save_file_name, file_model):
    headers = {
        'pragma': "no-cache",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=.",
        'upgrade-insecure-requests': "",
        'user-agent': "Mozilla/. (Windows NT .; WOW) AppleWebKit/. (KHTML, like Gecko) Chrome/... Safari/.",
        'accept': "text/html,application/xhtml+xml,application/xml;q=.,image/webp,image/apng,*/*;q=.",
        'cache-control': "no-cache",
        'connection': "keep-alive",
    }

    try:
        response = requests.request("GET", url, headers=headers)
        selector = etree.HTML(response.text, parser=etree.HTMLParser(encoding='utf-'))
    except Exception as e:
        print("页面加载失败", e)
    return_set = set()
    with open(save_file_name, file_model) as f:
        try:
            context = selector.xpath('//a/@href')
            for i in context:
                try:
                    if i[0] == "j":
                        continue
                    if i[1] == "/":
                        # print i
                        i = url + i.replace("/", "")
                        f.write(i)
                        f.write("\n")
                        return_set.add(i)
                        # print(len(return_set))
                        print(len(return_set), context[0], i)
                except Exception as e:
                    print("", e)
        except Exception as e:
            print("", e)
        return return_set


if __name__ == '__main__':  # 网页url采集爬虫，给定网址，以及存储文件，将该网页内全部网址采集下，可指定文件存储方式
    url = "https://www.aks.cn/"
    save_file_name = "url.txt"
    return_set = requests_for_url(url, save_file_name, "a")  # “a”:追加
    print(len(return_set))
