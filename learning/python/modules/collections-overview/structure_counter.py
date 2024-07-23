# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-22 01:34:46 UTC+08:00
"""

from collections import Counter

# 主要用于统计元素出现的次数

if __name__ == "__main__":
    words = ["apple", "banana", "apple", "orange", "banana", "pear", "apple"]
    staticist = Counter(words)
    print(staticist.most_common(2))
