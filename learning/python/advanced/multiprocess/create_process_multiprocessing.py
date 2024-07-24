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
import threading
from collections import deque


def task(count: int, container: deque):
    for i in range(count):
        container.append(i)
        time.sleep(1)


if __name__ == "__main__":
    print("单进程 单线程")
    single_start_time = time.time()
    data = deque()
    task(2, data)
    task(3, data)
    print(data)
    print(f"单进程 单线程 运行耗时: {time.time() - single_start_time}")

    print("单进程 多线程")
    multi_start_time = time.time()
    data2 = deque()
    t1 = threading.Thread(target=task, args=(2, data2))
    t2 = threading.Thread(target=task, args=(3, data2))
    t2.daemon = True
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    print(data2)
    print(f"单进程 多线程 运行耗时: {time.time() - multi_start_time}")
