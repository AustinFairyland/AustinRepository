# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-04 09:55:08 UTC+8
"""

import os
import shutil
from datetime import datetime

import pickle


def backup_and_copy(source, target):
    if os.path.exists(target):
        backup_dir = f"{target}_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        shutil.move(target, backup_dir)
        print(f"目标目录已存在，已备份到: {backup_dir}")

    try:
        shutil.copytree(source, target)
        print(f"目录从 {source} 复制到 {target} 完成。")
    except Exception as e:
        print(f"复制目录时出错: {e}")


if __name__ == "__main__":
    ...
    # source_dir = r"D:\developments\Repositories\personal\temp\text\tmp"
    # target_dir = r"D:\developments\Repositories\personal\temp\subscribes\tmp"
    # backup_and_copy(source_dir, target_dir)

    from typing import Literal
    
    mode = Literal["r", "rb", "w", "wb"]
    
    a = "r"
    print(isinstance(a, mode))
