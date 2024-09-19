# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-04 18:12:33 UTC+08:00
"""

import os
import shutil

from datetime import datetime


def cory_dir(source, target):
    if os.path.exists(target):
        backup_dir = f"{target}_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        shutil.move(target, backup_dir)
        print(f"目标目录已存在，已备份到: {backup_dir}")

    try:
        shutil.copytree(source, target)
        print(f"目录从 {source} 复制到 {target} 完成。")
    except Exception as err:
        print(f"复制目录时出错: {err}")


if __name__ == "__main__":
    cory_dir("/path/to/source/data", "/path/to/target/data")
