# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-22 16:46:34 UTC+08:00
"""

import os
import time
import multiprocessing


def watch():
    for i in range(3):
        print("看电视....", os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    # 启动一个进程
    print(os.getpid())
    process = multiprocessing.Process(target=watch)
    print(id(process), process)
    process.start()
