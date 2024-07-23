# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-21 23:58:13 UTC+08:00
"""

user_info = ('John',25, 'Male')

# 元组解包
name, age, gender = user_info
print(name, age, gender)

name, *others = user_info  # name: str, others: List, *others只能在最后一个位置
print(name, others, type(others))
