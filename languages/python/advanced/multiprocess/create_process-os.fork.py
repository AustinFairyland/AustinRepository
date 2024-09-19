# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-22 15:53:50 UTC+08:00
"""

import os

# 在 Linux 下执行

if __name__ == '__main__':
    w = 100
    pid = os.fork()  # 创建一个子进程
    print(f"1. 当前的进程是: {os.getpid()}")
    if pid == 0:
        print(f"2. 子进程: w={w}, 子进程ID={os.getpid()}, 当前子进程的父进程ID={os.getppid()}")
    else:
        print(f"3. 父进程: 当前进程PID: {os.getpid()}, 创建一个子进程ID={pid}")
