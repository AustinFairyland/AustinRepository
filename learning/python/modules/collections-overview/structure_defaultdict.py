# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-22 00:57:52 UTC+08:00
"""

from collections import defaultdict

if __name__ == "__main__":
    user_tuple = ("user1", "user2", "user3", "user4", "user2", "user3", "user4", "user1", "user5")

    # count the frequency of each user
    print("for loop count".center(50, "-"))
    user_dict = dict()
    for user in user_tuple:
        if user not in user_dict:
            user_dict.update({user: 1})
        else:
            user_dict.update({user: user_dict.get(user) + 1})
    print(user_dict)

    print("for loop count updated".center(50, "-"))
    user_dict2 = dict()
    for user in user_tuple:
        user_dict2.setdefault(user, 0)
        user_dict2.update({user: user_dict2.get(user) + 1})
    print(user_dict2)

    print("defaultdict count".center(50, "-"))
    user_defaultdict = defaultdict(int)
    for user in user_tuple:
        user_defaultdict[user] += 1
    print(user_defaultdict)
