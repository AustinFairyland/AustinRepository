# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-23 14:16:33 UTC+08:00
"""

import threading
import time

lock = threading.Lock()
generate_brick_list = [f"砖头{i}" for i in range(10)]
data_list = list()


class SafeQueue:

    def __init__(self, size: int):
        self.__item_list = list()
        self.size = size
        self.__item_lock = threading.Condition()

    def put(self, item):
        with self.__item_lock:
            while len(self.__item_list) >= self.size:
                self.__item_lock.wait()

            self.__item_list.insert(0, item)
            self.__item_lock.notify_all()

    def get(self):
        with self.__item_lock:
            while len(self.__item_list) == 0:
                self.__item_lock.wait()

            result = self.__item_list.pop()
            self.__item_lock.notify_all()

            return result


class MsgProducer(threading.Thread):
    def __init__(self, name: str, count: int, queue: SafeQueue):
        super().__init__()

        self.setName(name)
        self.count = count
        self.queue = queue

    def run(self) -> None:
        for n in range(self.count):
            msg = f"{self.getName()} - {n}"
            self.queue.put(msg)


class MsgConsumer(threading.Thread):
    def __init__(self, name: str, queue: SafeQueue):
        super().__init__()

        self.setName(name)
        self.queue = queue
        self.setDaemon(True)

    def run(self) -> None:
        while True:
            msg = self.queue.get()
            print(f"{self.getName()} - {msg}\n", end='')


def move_brick(brick):
    # print("开始搬砖".center(50, "*") + "\n", end="")
    print(f"正在搬砖: {brick}\n", end="")
    # print(f"{threading.currentThread()}, 休息1秒继续搬, 还剩下砖头数: {len(generate_brick_list)}\n", end="")
    time.sleep(1)


def main():
    threads = []
    for brick in generate_brick_list:
        for i in range(50):
            t = threading.Thread(target=move_brick, name=f"搬砖线程{i}", args=(brick,))
            t.start()
            threads.append(t)
    for t in threads:
        t.join()


if __name__ == '__main__':
    # print("10个线程开始搬砖")
    # a_start_time = time.time()
    # main()
    # print(f"总共耗时: {time.time() - a_start_time}秒")
    #
    # print("一个线程开始搬砖")
    # b_start_time = time.time()
    # for brick in generate_brick_list:
    #     move_brick(brick)
    # print(f"总共耗时: {time.time() - b_start_time}秒")
    queue = SafeQueue(3)
    threads = list()
    threads.append(MsgProducer("PA", 2, queue))
    threads.append(MsgProducer("PB", 2, queue))
    threads.append(MsgProducer("PC", 2, queue))

    threads.append(MsgConsumer("CA", queue))
    threads.append(MsgConsumer("CB", queue))

    for t in threads:
        t.start()

    time.sleep(100)
