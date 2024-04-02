# coding: utf8
"""
@ File: __main.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Linux Ubuntu 22.04.4 Kernel 6.2.0-36-generic 
@ CreatedTime: 2024/1/5
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

import string
import secrets

print(type(secrets.token_urlsafe(18)))
