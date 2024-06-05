# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-04-23 14:55:34 UTC+8
"""

from service.ExcelFileServices import ExcelBaseService
# from service.UserServices import UserServices
from service.FileServices import YamlFileService


# class CreateUser(object):
# 
#     @classmethod
#     def main(cls):
#         excel_path = r"D:\developments\Repositories\personal\project\python2.7\demo-001\data\users.xlsx"
#         excel_service = ExcelBaseService(excel_path)
# 
#         user_list = list()
#         for row in excel_service.get_all_data().__getitem__(slice(1, None)):
#             user_list.append(
#                 {
#                     'username': str(row.__getitem__(0)),
#                     'email': str(row.__getitem__(2)),
#                     'telephone': str(row.__getitem__(1)),
#                     'region': '全局数据域',
#                     'role': '文档管理,终端管理',
#                     'iprange': '*.*.*.*',
#                     # 'describe': '',
#                     'group': '全流量资产管理系统'
#                 }
#             )


class Test(object):

    @classmethod
    def main(cls):
        cls.t_1()

    @classmethod
    def t_1(cls):
        a = YamlFileService(r"D:\developments\Repositories\personal\project\python2.7\demo-001\conf\Asset-CMDB.yaml")
        content = a.read()
        print content, type(content)
        print content.get("event-rule-id"), type(content.get("event-rule-id"))


if __name__ == '__main__':
    Test.main()
