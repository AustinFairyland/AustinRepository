# coding: utf8
""" 
@File: RemoveRepeat.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-25
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time
import random

string = """CREATE TABLE internal_app_hnLt.load_balancing (id serial NOT NULL PRIMARY KEY, uuid varchar(255) NOT NULL, isOutline boolean DEFAULT true, create_time TIMESTAMP NULL, update_time TIMESTAMP NULL, system_id varchar(255) NOT NULL,responsible_department varchar(255) NOT NULL,person_in_charge_a varchar(255) NOT NULL,contact_information_responsible varchar(255) NOT NULL, "asset_main_ip" varchar(255)  NOT NULL,"equipment_name" varchar(255)  NOT NULL DEFAULT '负载均衡',"asset_type" varchar(255)  NOT NULL DEFAULT '负载均衡',"asset_subtype" varchar(255)  NOT NULL,"resource_domain" varchar(255)  NOT NULL,"asset_attribute" varchar(255)  NOT NULL,"port_and_protocol" varchar(255)  NOT NULL,"os_version" varchar(255)  NOT NULL,"hardware_manufacturer" varchar(255)  NOT NULL,"equipment_model" varchar(255)  NOT NULL,"firewall_version" varchar(255)  NOT NULL,"asset_name" varchar(255)  NOT NULL DEFAULT '负载均衡',"asset_rank" varchar(255)  NOT NULL,"graded_object_name" varchar(255) ,"net_unit_type" varchar(255) ,"internet_exposure_assets" varchar(255)  NOT NULL,"province" varchar(255)  NOT NULL,"city" varchar(255)  NOT NULL,"subordinate_department" varchar(255)  NOT NULL,"management_routing" varchar(255)  NOT NULL,"business_system" varchar(255)  NOT NULL,"business_name" varchar(255)  NOT NULL,"service_status" varchar(255)  NOT NULL,"region" varchar(255)  NOT NULL DEFAULT '核心区',"business_domain" varchar(255)  NOT NULL DEFAULT 'O域',"cabinet_position" varchar(255) ,"management_4a" varchar(255)  NOT NULL,"username" varchar(255) ,"password" varchar(255) ,"responsible_department" varchar(255)  NOT NULL,"person_in_charge_a" varchar(255)  NOT NULL,"contact_information_responsible" varchar(255)  NOT NULL,"maintenance_department" varchar(255)  NOT NULL,"maintenance_person" varchar(255)  NOT NULL,"contact_information_maintenance" varchar(255)  NOT NULL,"network_location" varchar(255)  NOT NULL,"brand_name" varchar(255)  NOT NULL,"brand_region" varchar(255)  NOT NULL,"hardware_environment" varchar(255)  NOT NULL,"software_environment" varchar(255)  NOT NULL)"""


import re

# def remove_duplicate_fields(sql_string):
#     field_pattern = re.compile(r'\"?(\w+)\"?\s+\w+')
#     seen_fields = set()
#     result_lines = []
#     lines = sql_string.split(',')
#     for line in lines:
#         match = field_pattern.search(line.strip())
#         if match:
#             field_name = match.group(1).lower()
#             if field_name not in seen_fields:
#                 seen_fields.add(field_name)
#                 result_lines.append(line)
#     return ',\n'.join(result_lines)


def remove_duplicate_fields(sql_string: str):
    new_string = sql_string.replace('"', " ")
    sql_keyworkd = new_string[: new_string.find("(")]
    a = new_string[new_string.find("(") + 1 : new_string.rfind(")")].split(",")
    print(sql_keyworkd)
    print(a)


cleaned_string = remove_duplicate_fields(string)
print(cleaned_string)

print(45 * 27 * 0.5 * 12)
