# coding: utf8
""" 
@File: setup.py
@Editor: PyCharm
@author: Lionel Johnson
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@datetime: 2023-12-31 00:00:00 UTC+08:00
"""

from distutils.core import setup
from Cython.Build import cythonize

if __name__ == '__main__':
    print('start')
    setup(ext_modules=cythonize(['util/del_files.py', 'util/initialize.py']))
