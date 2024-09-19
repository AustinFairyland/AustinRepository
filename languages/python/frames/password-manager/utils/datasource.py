# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-15 14:36:01 UTC+08:00
"""

from django.conf import settings

from fairylandfuture.modules.datasource import MySQLDataSource

_DATA_SOURCE_CONFG = settings.DATA_SOURCE_CONFIG

MySQLUtils = MySQLDataSource(
    host=_DATA_SOURCE_CONFG.get("host"),
    port=_DATA_SOURCE_CONFG.get("post"),
    user=_DATA_SOURCE_CONFG.get("username"),
    password=_DATA_SOURCE_CONFG.get("password"),
    database=_DATA_SOURCE_CONFG.get("database")
)
