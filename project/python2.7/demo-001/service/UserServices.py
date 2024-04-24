# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-04-23 14:20:23 UTC+8
"""

# BSA 批量创建用户接口
from permissionmanage.cur_models.usermodels import batch_create_user


class UserServices(object):

    @classmethod
    def create_users_batch(cls, user_list):
        return batch_create_user(user_list)


user_list = [
    {
        'username': '租户1',
        'email': '',
        'telephone': '13412345678',
        'region': '全局数据域',
        'role': '角色1',
        'iprange': '',
        'describe': '',
        'group': ''
    },
    {
        'username': '租户2',
        'email': '',
        'telephone': '13413345678',
        'region': '数据域1', 'role': '角色1',
        'iprange': '*.*.*.*',
        'describe': '',
        'group': ''
    }
]
# result =batch_create_user(user_list)
