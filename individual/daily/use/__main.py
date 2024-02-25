# coding: utf
"""
@ File: __main.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Linux Ubuntu .. Kernel ..--generic 
@ CreatedTime: //
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from typing import Union


class Comparison:

    @staticmethod
    def interval_range(integer: Union[int, float], _min: Union[int, float], _max: Union[int, float]) -> bool:
        if integer.__le__(_max) and integer.__ge__(_min):
            return True
        else:
            return False


class Main:

    @staticmethod
    def run() -> None:
        port = 52000
        min_port = 51000
        max_port = 52999
        results = Comparison.interval_range(port, min_port, max_port)
        print(results)


if __name__ == "__main__":
    Main.run()
