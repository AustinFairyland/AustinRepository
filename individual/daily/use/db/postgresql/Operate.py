# coding: utf8
""" 
@File: Operate.py
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

from typing import Union
import psycopg2


class ConnectPostgreSQL:
    def __init__(
        self,
        host: Union[str, None] = None,
        username: Union[str, None] = None,
        password: Union[str, None] = None,
        port: Union[int, None] = None,
        database: Union[str, None] = None,
    ):
        self.__host = host if host else "127.0.0.1"
        self.__username = username if username else "postgres"
        self.__password = password if password else ""
        self.__port = port if port else 5432
        self.__database = database if database else "postgres"

    def __connection(self):
        try:
            connection = psycopg2.connect(
                host=self.__host,
                user=self.__username,
                password=self.__password,
                port=self.__port,
                database=self.__database,
            )
        except Exception as error:
            pass
        else:
            return connection
        return None

    def __enter__(self):
        # return self.__connection()
        return 123

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__connection():
            self.__connection().close()
        return 123


if __name__ == "__main__":
    print(ConnectPostgreSQL())
