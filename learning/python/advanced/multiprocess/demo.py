# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-22 14:05:55 UTC+08:00
"""

import os
import time

if __name__ == '__main__':
    for i in range(60):
        time.sleep(1)

        print(f"{i}: 父进程: {os.getppid()}, 进程: {os.getpid()}".center(50, "-"))
