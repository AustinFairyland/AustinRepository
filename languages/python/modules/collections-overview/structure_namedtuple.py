# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-22 00:25:41 UTC+08:00
"""

from collections import namedtuple


class User:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


UserInfo = namedtuple("UserInfo", ["name", "age", "gender"])


if __name__ == "__main__":
    print("`class`".center(40, "="))
    user = User("John", 25, "Male")
    print(user.name, user.age, user.gender)

    print("`namedtuple`--tuple".center(40, "="))
    user_data = ("John", 25, "Male")
    user_info = UserInfo(*user_data)
    print(user_info.name, user_info.age, user_info.gender)

    print("`namedtuple`--dict".center(40, "="))
    user_dict = {"name": "John", "age": 25, "gender": "Male"}
    user_info = UserInfo(**user_dict)
    print(user_info.name, user_info.age, user_info.gender)

    print("`namedtuple`--multiple data".center(40, "="))
    user_columns = ("name", "age", "gender", "country")
    user_multiple_data = (("John", 25, "Male", "USA"), ("Mary", 30, "Female", "China"))
    user_multiple_info = map(lambda x: namedtuple("UserInfo", user_columns)(*x), user_multiple_data)
    print(tuple(user_info))
    for user in user_multiple_info:
        print(user.name, user.age, user.gender, user.country)
