# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-09 14:33:15 UTC+8
"""

from abc import ABCMeta, abstractmethod
from typing import Dict


class SingletonMeta(ABCMeta):
    _instances: Dict[type, object] = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances.update({cls: super().__call__(*args, **kwargs)})
        return cls._instances.get(cls)


class GenerateSQLBase(metaclass=SingletonMeta):

    @abstractmethod
    def generate(self, *args, **kwargs):
        pass


class GetData1(GenerateSQLBase):

    def generate(cls, *args, **kwargs):
        pass


class GetData2(GenerateSQLBase):
    def generate(self):
        return "2"


class GetData3(GenerateSQLBase):

    def generate(self, *args, **kwargs):
        return "aa"


if __name__ == '__main__':
    get_data_1 = GetData1()
    get_data_1_1 = GetData1()
    get_data_2 = GetData2()
    get_data_2_1 = GetData2()
    get_data_3 = GetData3()

    print(id(get_data_1), id(get_data_1_1))
    print(id(get_data_2), id(get_data_2_1))

    print(get_data_1.generate())
    print(get_data_1_1.generate())
    print(get_data_2.generate())

    print(GetData1.generate())
