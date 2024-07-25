# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-25 14:16:15 UTC+08:00
"""

if __name__ == '__main__':
    sql = (
        "select "
        "internal_app_permission.tb_user_group.id::int, "
        "internal_app_permission.tb_user_group.name::varchar "
        "from internal_app_permission.tb_user_group "
        "inner join internal_app_permission.tb_user_group_tree "
        "on internal_app_permission.tb_user_group_tree.user_group_id = internal_app_permission.tb_user_group.id "
        "inner join (select internal_app_permission.tb_user_group.id "
        "from internal_app_permission.tb_user_group "
        "where internal_app_permission.tb_user_group.name = '全流量资产管理系统') as temp "
        "on temp.id = internal_app_permission.tb_user_group_tree.parent_id;"
    )
    print(sql)
