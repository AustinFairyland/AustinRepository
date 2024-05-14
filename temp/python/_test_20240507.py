# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-07 14:32:48 UTC+8
"""

title_ls = ["系统编号", "系统名称", "系统描述", "已具备的防护手段", "选择项", "生命周期", "建设厂家", "建设时间", "交维情况", "交维时间", "维保情况", "维保起止时间", "是否定级备案", "定级单元名称", "定级备案级别", "定级备案时间", "系统网络拓扑图", "定级备案报告", "风险评估报告", "符合性评测", "建设规划所属单位", "系统维护所属单位", "系统维护负责人", "联系方式（负责人）", "系统维护所属部门", "运维维护负责单位", "运维维护负责人", "联系方式（运维）", "运维维护所属部门", "应用维护负责单位", "应用维护负责人", "联系方式（应用）", "应用维护所属部门", "硬件维护负责单位", "硬件维护负责人", "联系方式（硬件）", "硬件维护所属部门", "机房管理负责单位", "机房管理负责人", "联系方式（机房）", "机房管理所属部门", "建设规划负责单位", "建设规划负责人", "建设规划负责人联系方式"]
field_ls = ["system_id", "system_name", "system_description", "protecting_measures", "select_item", "lifecycle", "manufacturer", "time_of_production", "maintenance_of_handover", "handover_time", "warranty_condition", "warranty_period", "record_condition", "grading_unit", "grading_rank", "grading_time", "system_network_topo", "grading_report", "risk_evaluation_report", "compliance_evaluation", "subordinate_department_equipment", "responsible_department", "person_in_charge_a", "contact_information_responsible", "subordinate_department_system", "operation_maintenance_responsible_unit", "person_in_charge_operation", "contact_information_operation", "subordinate_department_operation", "use_maintenance_responsible_unit", "person_in_charge_use", "contact_information_use", "subordinate_department_use", "hardware_maintenance_responsible_unit", "person_in_charge_hardware", "contact_information_hardware", "subordinate_department_hardware", "computerroom_management_responsible_unit", "person_in_charge_computerroom", "contact_information_computerroom", "subordinate_department_computerroom", "construction_planning_responsible_unit", "person_in_charge_construction", "subordinate_department_construction"]
require_ls = [
    "必填项\n\n从HA-001开始手工分配，并且可编辑，一旦出现退网系统，空出编号即可", 
    "必填项", 
    "必填项", 
    "非必填项\n\n如防火墙、WAF、IPS等", 
    "非必填项", "必填项", "必填项", "必填项", "必填项", "非必填项", "必填项", "非必填项", "必填项", "非必填项", "非必填项", "非必填项", "非必填项", "非必填项", "非必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "非必填项", "非必填项", "非必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "非必填项", "非必填项", "非必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项", "必填项"]

print(title_ls.__len__(), field_ls.__len__(), require_ls.__len__())

a = zip_list = [(title, field) for  title, field in zip(title_ls, field_ls)]
# aa = list()
# bb = list()
# for title, field in a:
#     aa.append(title)
#     bb.append(field)
aa, bb = zip(*a)
print(aa, "\n", bb)

# subordinate_department_system = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "系统维护所属单位" else None for item in a]
# )).__getitem__(0)

# print(subordinate_department_system)

# responsible_department_index, _ = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "系统维护所属部室" else None for item in a]
# )).__getitem__(0)
# a.pop(subordinate_department_system_index)
# a.insert(responsible_department_index, subordinate_department_system)

# subordinate_department_system_index, subordinate_department_system = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "系统维护所属单位" else None for item in a]
# )).__getitem__(0)
# responsible_department_index, _ = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "系统维护所属部室" else None for item in a]
# )).__getitem__(0)
# a.pop(subordinate_department_system_index)
# a.insert(responsible_department_index, subordinate_department_system)
# subordinate_department_operation_index, subordinate_department_operation = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "应用维护所属单位" else None for item in a]
# )).__getitem__(0)
# operation_maintenance_responsible_unit_index, _ = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "应用维护所属部室" else None for item in a]
# )).__getitem__(0)
# a.pop(subordinate_department_operation_index)
# a.insert(operation_maintenance_responsible_unit_index, subordinate_department_operation)
# 
# subordinate_department_use_index, subordinate_department_use = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "运营使用所属单位" else None for item in a]
# )).__getitem__(0)
# use_maintenance_responsible_unit_index, _ = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "运营使用所属部室" else None for item in a]
# )).__getitem__(0)
# a.pop(subordinate_department_use_index)
# a.insert(use_maintenance_responsible_unit_index, subordinate_department_use)
# 
# subordinate_department_hardware_index, subordinate_department_hardware = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "硬件维护所属单位" else None for item in a]
# )).__getitem__(0)
# hardware_maintenance_responsible_unit_index, _ = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "硬件维护所属部室" else None for item in a]
# )).__getitem__(0)
# a.pop(subordinate_department_hardware_index)
# a.insert(hardware_maintenance_responsible_unit_index, subordinate_department_hardware)
# 
# subordinate_department_computerroom_index, subordinate_department_computerroom = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "机房管理所属单位" else None for item in a]
# )).__getitem__(0)
# computerroom_management_responsible_unit, _ = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "机房管理所属部室" else None for item in a]
# )).__getitem__(0)
# a.pop(subordinate_department_computerroom_index)
# a.insert(computerroom_management_responsible_unit, subordinate_department_computerroom)
# 
# subordinate_department_equipment_index, subordinate_department_equipment = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "建设规划所属单位" else None for item in a]
# )).__getitem__(0)
# construction_planning_responsible_unit_index, _ = list(filter(
#     lambda x: x,
#     [(a.index(item), item) if str(item.__getitem__(0)) == "建设规划所属部室" else None for item in a]
# )).__getitem__(0)
# a.pop(subordinate_department_equipment_index)
# a.insert(construction_planning_responsible_unit_index - 1, subordinate_department_equipment)









