# coding: utf8
""" 
@File: BuilderSecretKey.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-20
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

import secrets
from typing import Union


class BuilderSecretKey:
    @classmethod
    def token(cls, length: int = 18, prefix: Union[str, None] = None) -> str:
        if prefix:
            return "_".join((prefix, secrets.token_urlsafe(length)))
        else:
            return secrets.token_urlsafe(length)


if __name__ == "__main__":
    print(BuilderSecretKey.token(prefix="ast", length=22))
