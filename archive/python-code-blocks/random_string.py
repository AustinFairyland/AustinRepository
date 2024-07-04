# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-04 18:20:38 UTC+8
"""

import random
import string

def random_string(min_length=4, max_length=10):
    length = random.randint(min_length, max_length)
    random_char = string.ascii_letters + string.digits
    return ''.join(random.choices(random_char, k=length))
