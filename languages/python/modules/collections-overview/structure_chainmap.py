# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-22 01:45:32 UTC+08:00
"""

from collections import ChainMap

if __name__ == "__main__":
    user_dict = {"name": "John", "age": 25}
    user_dict2 = {"city": "New York", "country": "USA"}
    chain_map = ChainMap(user_dict, user_dict2)
    for k, v in chain_map.items():
        print(k, v)
