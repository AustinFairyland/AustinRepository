# coding: utf8
""" 
@File: main.py
@Editor: PyCharm
@author: Lionel Johnson
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@datetime: 2023-12-31 00:00:00 UTC+08:00
"""

from util import del_file
import sys

if __name__ == '__main__':
    try:
        stats = sys.argv[1]
        if stats == 'del':
            del_file(enable=True)
    except IndexError:
        del_file()
