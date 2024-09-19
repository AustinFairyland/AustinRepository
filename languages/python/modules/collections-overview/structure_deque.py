# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-22 01:14:28 UTC+08:00
"""

# deque -> Double-ended queue 双端队列
# 对于 List 是线程不安全的, 而对于 deque 是线程安全的.

from collections import deque

if __name__ == '__main__':
    user_list = ['Alice', 'Bob', 'Charlie', 'David']

    print("End element".center(50, '-'))
    username = user_list.pop()
    print(username, user_list)
    user_list.append(username)

    print("deque init".center(50, '-'))
    user_deque = deque(user_list)
    print(user_deque)
