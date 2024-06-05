# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-06 17:13:54 UTC+8
"""

tmp_list = [["1"], ["2"], ["3"]]
subasset_uuid_list = [uuid for row in tmp_list for uuid in row]
print(subasset_uuid_list)
