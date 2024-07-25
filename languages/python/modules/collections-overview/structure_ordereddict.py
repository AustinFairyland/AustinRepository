# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-22 01:42:21 UTC+08:00
"""

from collections import OrderedDict

# 有序字典
# 字典是无序的，而有序字典则是有序的。
# 有序字典的键值对会按照插入的顺序排列。

if __name__ == '__main__':
    user_dict = OrderedDict({'name': 'John', 'age': 25, 'city': 'New York'})
    user_dict.update(height=175, weight=70)
    print(user_dict, isinstance(user_dict, dict))
