# coding: utf8
""" 
@File: __init__.py
@Editor: PyCharm
@author: Lionel Johnson
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@datetime: 2023-12-31 00:00:00 UTC+08:00
"""

from .del_files import DelFiles


def del_file(enable=False): DelFiles().filter(enable)
