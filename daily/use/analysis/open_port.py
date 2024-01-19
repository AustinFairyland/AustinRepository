# coding: utf8
""" 
@File: open_port.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-19
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

import time
import random

import re


class AnalyseOpenPort:
    @staticmethod
    def __obtain_file_content(file_name: str):
        with open(file=file_name, mode="r", encoding="utf8") as scan_file:
            for line in scan_file:
                yield line

    @classmethod
    def __obtain_open_port(cls, file_name: str):
        results = list()
        for line in cls.__obtain_file_content(file_name):
            if line.startswith("Discovered open port"):
                match = re.search(r"(\d+)", line)
                results.append(match.group())
        results.sort(key=lambda x: int(x))
        return tuple(results)

    @classmethod
    def __output_file(
        cls,
        content: str,
        output_path: str | None = None,
        file_name: str | None = None,
        file_ext_name: str | None = None,
        clear_file: bool = False,
    ):
        if not output_path:
            output_path = "./output"
        if not file_name:
            file_name = "output"
        if not file_ext_name:
            file_ext_name = "txt"
        file_full_name = ".".join((file_name, file_ext_name))
        file_full_path = os.path.join(output_path, file_full_name)
        if clear_file:
            cls.__clear_content(file_full_path)
        with open(file=file_full_path, mode="a+", encoding="utf8") as output_file:
            for line in str(content).split("\n"):
                output_file.write(line)
                output_file.write("\n")

    @classmethod
    def __clear_content(cls, file_full_path):
        with open(file=file_full_path, mode="w", encoding="utf8") as file:
            file.write("")

    @classmethod
    def run(cls):
        mapping_port = cls.__obtain_open_port(
            "./data/nmap-scan-mapping.fairies.ltd.txt"
        )
        cloud_port = cls.__obtain_open_port("./data/nmap-scan-cloud.fairies.ltd.txt")
        cls.__output_file("mapping.fairies.ltd 开放端口", clear_file=True)
        for element in mapping_port:
            cls.__output_file(element)
        cls.__output_file("cloud.fairies.ltd 开放端口")
        for element in cloud_port:
            cls.__output_file(element)


if __name__ == "__main__":
    AnalyseOpenPort.run()
