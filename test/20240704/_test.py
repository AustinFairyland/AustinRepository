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
import pickle
import random
import glob

from datetime import datetime
from string import ascii_letters, digits


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


def random_name(min_length=4, max_length=10):
    length = random.randint(min_length, max_length)
    random_char = ascii_letters + digits
    return ''.join(random.choices(random_char, k=length))


def make_dir(dir_path, dir_names):
    for dir_name in dir_names:
        new_dir_path = os.path.join(dir_path, dir_name)
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path, exist_ok=True)
            print(f"OK: {new_dir_path}")
            
def make_file(dir_path, file_names):
    all_dir_list = [path for path in glob.glob(f"{dir_path}{os.sep}**", recursive=True) if os.path.isdir(path)]
    for file_name in file_names:
        file_path = f"{os.sep}".join((random.choices(all_dir_list, k=1)[0], file_name))
        open(file_path, "w").close()
        print(f"OK: {file_path}")


if __name__ == "__main__":
    ...
    # source_dir = r"D:\developments\Repositories\personal\temp\text\tmp"
    # target_dir = r"D:\developments\Repositories\personal\temp\subscribes\tmp"
    # backup_and_copy(source_dir, target_dir)

    # 创建一些测试文件
    # make_dir(r"D:\developments\Repositories\personal\test\20240704\src_dir", [random_name() for _ in range(10)])
    # make_dir(r"D:\developments\Repositories\personal\test\20240704\dst_dir", [random_name() for _ in range(10)])
    # make_file(r"D:\developments\Repositories\personal\test\20240704\src_dir", [random_name() for _ in range(50)])
    # make_file(r"D:\developments\Repositories\personal\test\20240704\dst_dir", [random_name() for _ in range(50)])

    source_dir = r"D:\developments\Repositories\personal\test\20240704\src_dir\2DQG"
    target_dir = r"D:\developments\Repositories\personal\test\20240704\dst_dir\6eOPIAcPY\2DQG"
    backup_and_copy(source_dir, target_dir)
