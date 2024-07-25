# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-23 12:24:09 UTC+08:00
"""

import time
from threading import Thread


class SimpleDemo:

    @classmethod
    def run(cls):
        time.sleep(3)


if __name__ == '__main__':
    print("单进程单线程执行2次".center(50, "="))
    single_start_time = time.time()
    SimpleDemo.run()
    SimpleDemo.run()
    print(f"单进程单线程执行完毕，耗时：{time.time() - single_start_time:.5f}s".center(50, "="))

    print("单进程多线程执行2次(2个线程并发)".center(50, "="))
    multi_start_time = time.time()
    t1 = Thread(target=SimpleDemo.run)
    t2 = Thread(target=SimpleDemo.run)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"单进程多线程执行完毕，耗时：{time.time() - multi_start_time:.5f}s".center(50, "="))
