# coding: utf8
""" 
@File: AnalysisLogs.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-25
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from glob import glob


class AnalysisLogs:
    @classmethod
    def obtain_content(cls):
        for path_ in glob("./data/**/*"):
            if not os.path.isdir(path_):
                for line in cls.__obtain_file_content(os.path.normpath(path_)):
                    if (
                        "delete" in line.lower()
                        and "urls.py" not in line.lower()
                        and "search_data" not in line.lower()
                    ):
                        cls.output(content=line, mode="a+")
                        # if "tbl_meta_page_relation" in line.lower():

    @staticmethod
    def __obtain_file_content(file_name: str):
        with open(file=file_name, mode="r", encoding="utf8") as scan_file:
            for line in scan_file:
                yield line

    @classmethod
    def output(cls, file_path="./output/output.log", content="", mode="w"):
        with open(file_path, mode=mode) as file:
            file.write(content)

    @classmethod
    def run(cls):
        cls.obtain_content()


if __name__ == "__main__":
    AnalysisLogs.run()
