# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-22 10:16:32 UTC+08:00
"""

from collections import OrderedDict
from types import MappingProxyType

if __name__ == '__main__':
    test_dict = OrderedDict({"user": "admin", "age": 10})
    test_dict.update(gender="Male")
