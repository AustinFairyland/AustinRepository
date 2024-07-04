# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-04 18:21:52 UTC+8
"""

import os


def create_dir(dir_path, dir_names):
    for dir_name in dir_names:
        new_dir_path = os.path.join(dir_path, dir_name)
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path, exist_ok=True)
            print(f"OK: {new_dir_path}")
            
