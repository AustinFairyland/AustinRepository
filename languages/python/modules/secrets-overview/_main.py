# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-09-24 10:44:06 UTC+08:00
"""

import secrets
import base64

secret_token = secrets.token_bytes(32)
print(secret_token)
print(base64.b64encode(secret_token).decode())

start_time, end_time = 1727107200000, 1727107200000
current_time = 1727169201000
print(start_time <= current_time <= end_time)
print(current_time in range(start_time, end_time + 1))
