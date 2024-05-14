# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-04-26 10:46:50 UTC+8
"""

import locale


def test_01():
    locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')
    strings = (
        '联通集团公司\联通智网创新中心,'
        '河南省分公司本部\市场部,'
        '河南省分公司本部\数字化部,'
        '河南省分公司本部\网络部,'
        '河南省分公司本部\网络与信息安全部,'
        '河南省分公司本部\云网运营中心,'
        '河南省分公司本部\移网运营中心,'
        '河南省分公司本部\中部大区运营中心,'
        '安阳市分公司,'
        '鹤壁市分公司,'
        '济源市分公司,'
        '焦作市分公司,'
        '开封市分公司,'
        '洛阳市分公司,'
        '南阳市分公司,'
        '平顶山市分公司,'
        '濮阳市分公司,'
        '三门峡市分公司,'
        '商丘市分公司,'
        '新乡市分公司,'
        '信阳市分公司,'
        '许昌市分公司,'
        '郑州市分公司,'
        '周口市分公司,'
        '驻马店市分公司'
    )
    # src_strings_list = strings.split(',')
    # sorted_strings_list = sorted(src_strings_list, key=locale.strxfrm)
    re_list = list()
    print(strings)
    for i, string in enumerate(strings.split(',')):
        re_list.append({
            "value": i,
            "label": string
        })

    print(re_list)


def test_02():
    a = [
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "iconValue": "从HA-001开始手工分配，并且可编辑，一旦出现退网系统，空出编号即可",
            "inputType": "input",
            "key": "system_id",
            "label": "系统编号"
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "system_name",
            "label": "系统名称"
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "system_description",
            "label": "系统描述"
        },
        {
            "validators": [],
            "iconValue": "如防火墙、WAF、IPS等",
            "inputType": "input",
            "key": "protecting_measures",
            "label": "已具备的防护手段"
        },
        {
            "inputType": "select",
            "label": "是否纳入4A",
            "options": [
                {
                    "value": 0,
                    "label": "是"
                },
                {
                    "value": 1,
                    "label": "否"
                }
            ],
            "key": "select_item",
            "validators": []
        },
        {
            "inputType": "select",
            "label": "生命周期",
            "options": [
                {
                    "value": 0,
                    "label": "调试"
                },
                {
                    "value": 1,
                    "label": "上线"
                },
                {
                    "value": 2,
                    "label": "试运行"
                },
                {
                    "value": 3,
                    "label": "正式运行"
                },
                {
                    "value": 4,
                    "label": "退网"
                }
            ],
            "key": "lifecycle",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "manufacturer",
            "label": "建设厂家"
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "date-picker",
            "key": "time_of_production",
            "label": "建设时间"
        },
        {
            "inputType": "select",
            "label": "交维情况",
            "options": [
                {
                    "value": 0,
                    "label": "在建"
                },
                {
                    "value": 1,
                    "label": "未交维"
                },
                {
                    "value": 2,
                    "label": "已交维"
                },
                {
                    "value": 3,
                    "label": "运维期"
                }
            ],
            "key": "maintenance_of_handover",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [],
            "inputType": "date-picker",
            "key": "handover_time",
            "label": "交维时间"
        },
        {
            "inputType": "select",
            "label": "维保情况",
            "options": [
                {
                    "value": 0,
                    "label": "质保期"
                },
                {
                    "value": 1,
                    "label": "维保期"
                },
                {
                    "value": 2,
                    "label": "无维保"
                }
            ],
            "key": "warranty_condition",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [],
            "inputType": "date-picker",
            "key": "warranty_period",
            "label": "维保起止时间"
        },
        {
            "inputType": "select",
            "label": "是否定级备案",
            "options": [
                {
                    "value": 0,
                    "label": "是"
                },
                {
                    "value": 1,
                    "label": "否"
                }
            ],
            "key": "record_condition",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [],
            "inputType": "input",
            "key": "grading_unit",
            "label": "定级单元名称"
        },
        {
            "inputType": "select",
            "label": "定级备案级别",
            "options": [
                {
                    "value": 0,
                    "label": "第1级"
                },
                {
                    "value": 1,
                    "label": "第2级"
                },
                {
                    "value": 2,
                    "label": "第3级"
                },
                {
                    "value": 3,
                    "label": "第4级"
                },
                {
                    "value": 4,
                    "label": "第5级"
                }
            ],
            "key": "grading_rank",
            "validators": []
        },
        {
            "validators": [],
            "inputType": "date-picker",
            "key": "grading_time",
            "label": "定级备案时间"
        },
        {
            "validators": [],
            "inputType": "upload",
            "key": "system_network_topo",
            "label": "系统网络拓扑图"
        },
        {
            "validators": [],
            "inputType": "upload",
            "key": "grading_report",
            "label": "定级备案报告"
        },
        {
            "validators": [],
            "inputType": "upload",
            "key": "risk_evaluation_report",
            "label": "风险评估报告"
        },
        {
            "validators": [],
            "inputType": "upload",
            "key": "compliance_evaluation",
            "label": "符合性评测"
        },
        {
            "value": 5,
            "label": "建设规划所属单位",
            "options": [
                {
                    "value": 0,
                    "label": "联通集团公司\\联通智网创新中心"
                },
                {
                    "value": 1,
                    "label": "河南省分公司本部\\市场部"
                },
                {
                    "value": 2,
                    "label": "河南省分公司本部\\数字化部"
                },
                {
                    "value": 3,
                    "label": "河南省分公司本部\\网络部"
                },
                {
                    "value": 4,
                    "label": "河南省分公司本部\\网络与信息安全部"
                },
                {
                    "value": 5,
                    "label": "河南省分公司本部\\云网运营中心"
                },
                {
                    "value": 6,
                    "label": "河南省分公司本部\\移网运营中心"
                },
                {
                    "value": 7,
                    "label": "河南省分公司本部\\中部大区运营中心"
                },
                {
                    "value": 8,
                    "label": "安阳市分公司"
                },
                {
                    "value": 9,
                    "label": "鹤壁市分公司"
                },
                {
                    "value": 10,
                    "label": "济源市分公司"
                },
                {
                    "value": 11,
                    "label": "焦作市分公司"
                },
                {
                    "value": 12,
                    "label": "开封市分公司"
                },
                {
                    "value": 13,
                    "label": "洛阳市分公司"
                },
                {
                    "value": 14,
                    "label": "南阳市分公司"
                },
                {
                    "value": 15,
                    "label": "平顶山市分公司"
                },
                {
                    "value": 16,
                    "label": "濮阳市分公司"
                },
                {
                    "value": 17,
                    "label": "三门峡市分公司"
                },
                {
                    "value": 18,
                    "label": "商丘市分公司"
                },
                {
                    "value": 19,
                    "label": "新乡市分公司"
                },
                {
                    "value": 20,
                    "label": "信阳市分公司"
                },
                {
                    "value": 21,
                    "label": "许昌市分公司"
                },
                {
                    "value": 22,
                    "label": "郑州市分公司"
                },
                {
                    "value": 23,
                    "label": "周口市分公司"
                },
                {
                    "value": 24,
                    "label": "驻马店市分公司"
                }
            ],
            "key": "subordinate_department_equipment",
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "select"
        },
        {
            "inputType": "select",
            "label": "系统维护所属部室",
            "options": [
                {
                    "value": 0,
                    "label": "部室"
                }
            ],
            "key": "responsible_department",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "person_in_charge_a",
            "label": "系统维护责任人"
        },
        {
            "validators": [
                {
                    "value": "^(1)\\d{10}$",
                    "label": "customReg"
                },
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "contact_information_responsible",
            "label": "系统维护责任人联系方式"
        },
        {
            "value": 5,
            "label": "系统维护所属单位",
            "options": [
                {
                    "value": 0,
                    "label": "联通集团公司\\联通智网创新中心"
                },
                {
                    "value": 1,
                    "label": "河南省分公司本部\\市场部"
                },
                {
                    "value": 2,
                    "label": "河南省分公司本部\\数字化部"
                },
                {
                    "value": 3,
                    "label": "河南省分公司本部\\网络部"
                },
                {
                    "value": 4,
                    "label": "河南省分公司本部\\网络与信息安全部"
                },
                {
                    "value": 5,
                    "label": "河南省分公司本部\\云网运营中心"
                },
                {
                    "value": 6,
                    "label": "河南省分公司本部\\移网运营中心"
                },
                {
                    "value": 7,
                    "label": "河南省分公司本部\\中部大区运营中心"
                },
                {
                    "value": 8,
                    "label": "安阳市分公司"
                },
                {
                    "value": 9,
                    "label": "鹤壁市分公司"
                },
                {
                    "value": 10,
                    "label": "济源市分公司"
                },
                {
                    "value": 11,
                    "label": "焦作市分公司"
                },
                {
                    "value": 12,
                    "label": "开封市分公司"
                },
                {
                    "value": 13,
                    "label": "洛阳市分公司"
                },
                {
                    "value": 14,
                    "label": "南阳市分公司"
                },
                {
                    "value": 15,
                    "label": "平顶山市分公司"
                },
                {
                    "value": 16,
                    "label": "濮阳市分公司"
                },
                {
                    "value": 17,
                    "label": "三门峡市分公司"
                },
                {
                    "value": 18,
                    "label": "商丘市分公司"
                },
                {
                    "value": 19,
                    "label": "新乡市分公司"
                },
                {
                    "value": 20,
                    "label": "信阳市分公司"
                },
                {
                    "value": 21,
                    "label": "许昌市分公司"
                },
                {
                    "value": 22,
                    "label": "郑州市分公司"
                },
                {
                    "value": 23,
                    "label": "周口市分公司"
                },
                {
                    "value": 24,
                    "label": "驻马店市分公司"
                }
            ],
            "key": "subordinate_department_system",
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "select"
        },
        {
            "inputType": "select",
            "label": "应用维护所属部室",
            "options": [
                {
                    "value": 0,
                    "label": "部室"
                }
            ],
            "key": "operation_maintenance_responsible_unit",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "person_in_charge_operation",
            "label": "应用维护责任人"
        },
        {
            "validators": [
                {
                    "value": "^(1)\\d{10}$",
                    "label": "customReg"
                },
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "contact_information_operation",
            "label": "应用维护责任人联系方式"
        },
        {
            "value": 5,
            "label": "应用维护所属单位",
            "options": [
                {
                    "value": 0,
                    "label": "联通集团公司\\联通智网创新中心"
                },
                {
                    "value": 1,
                    "label": "河南省分公司本部\\市场部"
                },
                {
                    "value": 2,
                    "label": "河南省分公司本部\\数字化部"
                },
                {
                    "value": 3,
                    "label": "河南省分公司本部\\网络部"
                },
                {
                    "value": 4,
                    "label": "河南省分公司本部\\网络与信息安全部"
                },
                {
                    "value": 5,
                    "label": "河南省分公司本部\\云网运营中心"
                },
                {
                    "value": 6,
                    "label": "河南省分公司本部\\移网运营中心"
                },
                {
                    "value": 7,
                    "label": "河南省分公司本部\\中部大区运营中心"
                },
                {
                    "value": 8,
                    "label": "安阳市分公司"
                },
                {
                    "value": 9,
                    "label": "鹤壁市分公司"
                },
                {
                    "value": 10,
                    "label": "济源市分公司"
                },
                {
                    "value": 11,
                    "label": "焦作市分公司"
                },
                {
                    "value": 12,
                    "label": "开封市分公司"
                },
                {
                    "value": 13,
                    "label": "洛阳市分公司"
                },
                {
                    "value": 14,
                    "label": "南阳市分公司"
                },
                {
                    "value": 15,
                    "label": "平顶山市分公司"
                },
                {
                    "value": 16,
                    "label": "濮阳市分公司"
                },
                {
                    "value": 17,
                    "label": "三门峡市分公司"
                },
                {
                    "value": 18,
                    "label": "商丘市分公司"
                },
                {
                    "value": 19,
                    "label": "新乡市分公司"
                },
                {
                    "value": 20,
                    "label": "信阳市分公司"
                },
                {
                    "value": 21,
                    "label": "许昌市分公司"
                },
                {
                    "value": 22,
                    "label": "郑州市分公司"
                },
                {
                    "value": 23,
                    "label": "周口市分公司"
                },
                {
                    "value": 24,
                    "label": "驻马店市分公司"
                }
            ],
            "key": "subordinate_department_operation",
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "select"
        },
        {
            "inputType": "select",
            "label": "运营使用所属部室",
            "options": [
                {
                    "value": 0,
                    "label": "部室"
                }
            ],
            "key": "use_maintenance_responsible_unit",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "person_in_charge_use",
            "label": "运营使用责任人"
        },
        {
            "validators": [
                {
                    "value": "^(1)\\d{10}$",
                    "label": "customReg"
                },
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "contact_information_use",
            "label": "运营使用责任人联系方式"
        },
        {
            "value": 5,
            "label": "运营使用所属单位",
            "options": [
                {
                    "value": 0,
                    "label": "联通集团公司\\联通智网创新中心"
                },
                {
                    "value": 1,
                    "label": "河南省分公司本部\\市场部"
                },
                {
                    "value": 2,
                    "label": "河南省分公司本部\\数字化部"
                },
                {
                    "value": 3,
                    "label": "河南省分公司本部\\网络部"
                },
                {
                    "value": 4,
                    "label": "河南省分公司本部\\网络与信息安全部"
                },
                {
                    "value": 5,
                    "label": "河南省分公司本部\\云网运营中心"
                },
                {
                    "value": 6,
                    "label": "河南省分公司本部\\移网运营中心"
                },
                {
                    "value": 7,
                    "label": "河南省分公司本部\\中部大区运营中心"
                },
                {
                    "value": 8,
                    "label": "安阳市分公司"
                },
                {
                    "value": 9,
                    "label": "鹤壁市分公司"
                },
                {
                    "value": 10,
                    "label": "济源市分公司"
                },
                {
                    "value": 11,
                    "label": "焦作市分公司"
                },
                {
                    "value": 12,
                    "label": "开封市分公司"
                },
                {
                    "value": 13,
                    "label": "洛阳市分公司"
                },
                {
                    "value": 14,
                    "label": "南阳市分公司"
                },
                {
                    "value": 15,
                    "label": "平顶山市分公司"
                },
                {
                    "value": 16,
                    "label": "濮阳市分公司"
                },
                {
                    "value": 17,
                    "label": "三门峡市分公司"
                },
                {
                    "value": 18,
                    "label": "商丘市分公司"
                },
                {
                    "value": 19,
                    "label": "新乡市分公司"
                },
                {
                    "value": 20,
                    "label": "信阳市分公司"
                },
                {
                    "value": 21,
                    "label": "许昌市分公司"
                },
                {
                    "value": 22,
                    "label": "郑州市分公司"
                },
                {
                    "value": 23,
                    "label": "周口市分公司"
                },
                {
                    "value": 24,
                    "label": "驻马店市分公司"
                }
            ],
            "key": "subordinate_department_use",
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "select"
        },
        {
            "inputType": "select",
            "label": "硬件维护所属部室",
            "options": [
                {
                    "value": 0,
                    "label": "部室"
                }
            ],
            "key": "hardware_maintenance_responsible_unit",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "person_in_charge_hardware",
            "label": "硬件维护责任人"
        },
        {
            "validators": [
                {
                    "value": "^(1)\\d{10}$",
                    "label": "customReg"
                },
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "contact_information_hardware",
            "label": "硬件维护责任人联系方式"
        },
        {
            "value": 5,
            "label": "硬件维护所属单位",
            "options": [
                {
                    "value": 0,
                    "label": "联通集团公司\\联通智网创新中心"
                },
                {
                    "value": 1,
                    "label": "河南省分公司本部\\市场部"
                },
                {
                    "value": 2,
                    "label": "河南省分公司本部\\数字化部"
                },
                {
                    "value": 3,
                    "label": "河南省分公司本部\\网络部"
                },
                {
                    "value": 4,
                    "label": "河南省分公司本部\\网络与信息安全部"
                },
                {
                    "value": 5,
                    "label": "河南省分公司本部\\云网运营中心"
                },
                {
                    "value": 6,
                    "label": "河南省分公司本部\\移网运营中心"
                },
                {
                    "value": 7,
                    "label": "河南省分公司本部\\中部大区运营中心"
                },
                {
                    "value": 8,
                    "label": "安阳市分公司"
                },
                {
                    "value": 9,
                    "label": "鹤壁市分公司"
                },
                {
                    "value": 10,
                    "label": "济源市分公司"
                },
                {
                    "value": 11,
                    "label": "焦作市分公司"
                },
                {
                    "value": 12,
                    "label": "开封市分公司"
                },
                {
                    "value": 13,
                    "label": "洛阳市分公司"
                },
                {
                    "value": 14,
                    "label": "南阳市分公司"
                },
                {
                    "value": 15,
                    "label": "平顶山市分公司"
                },
                {
                    "value": 16,
                    "label": "濮阳市分公司"
                },
                {
                    "value": 17,
                    "label": "三门峡市分公司"
                },
                {
                    "value": 18,
                    "label": "商丘市分公司"
                },
                {
                    "value": 19,
                    "label": "新乡市分公司"
                },
                {
                    "value": 20,
                    "label": "信阳市分公司"
                },
                {
                    "value": 21,
                    "label": "许昌市分公司"
                },
                {
                    "value": 22,
                    "label": "郑州市分公司"
                },
                {
                    "value": 23,
                    "label": "周口市分公司"
                },
                {
                    "value": 24,
                    "label": "驻马店市分公司"
                }
            ],
            "key": "subordinate_department_hardware",
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "select"
        },
        {
            "inputType": "select",
            "label": "机房管理所属部室",
            "options": [
                {
                    "value": 0,
                    "label": "部室"
                }
            ],
            "key": "computerroom_management_responsible_unit",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "person_in_charge_computerroom",
            "label": "机房管理责任人"
        },
        {
            "validators": [
                {
                    "value": "^(1)\\d{10}$",
                    "label": "customReg"
                },
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "contact_information_computerroom",
            "label": "机房管理责任人联系方式"
        },
        {
            "value": 5,
            "label": "机房管理所属单位",
            "options": [
                {
                    "value": 0,
                    "label": "联通集团公司\\联通智网创新中心"
                },
                {
                    "value": 1,
                    "label": "河南省分公司本部\\市场部"
                },
                {
                    "value": 2,
                    "label": "河南省分公司本部\\数字化部"
                },
                {
                    "value": 3,
                    "label": "河南省分公司本部\\网络部"
                },
                {
                    "value": 4,
                    "label": "河南省分公司本部\\网络与信息安全部"
                },
                {
                    "value": 5,
                    "label": "河南省分公司本部\\云网运营中心"
                },
                {
                    "value": 6,
                    "label": "河南省分公司本部\\移网运营中心"
                },
                {
                    "value": 7,
                    "label": "河南省分公司本部\\中部大区运营中心"
                },
                {
                    "value": 8,
                    "label": "安阳市分公司"
                },
                {
                    "value": 9,
                    "label": "鹤壁市分公司"
                },
                {
                    "value": 10,
                    "label": "济源市分公司"
                },
                {
                    "value": 11,
                    "label": "焦作市分公司"
                },
                {
                    "value": 12,
                    "label": "开封市分公司"
                },
                {
                    "value": 13,
                    "label": "洛阳市分公司"
                },
                {
                    "value": 14,
                    "label": "南阳市分公司"
                },
                {
                    "value": 15,
                    "label": "平顶山市分公司"
                },
                {
                    "value": 16,
                    "label": "濮阳市分公司"
                },
                {
                    "value": 17,
                    "label": "三门峡市分公司"
                },
                {
                    "value": 18,
                    "label": "商丘市分公司"
                },
                {
                    "value": 19,
                    "label": "新乡市分公司"
                },
                {
                    "value": 20,
                    "label": "信阳市分公司"
                },
                {
                    "value": 21,
                    "label": "许昌市分公司"
                },
                {
                    "value": 22,
                    "label": "郑州市分公司"
                },
                {
                    "value": 23,
                    "label": "周口市分公司"
                },
                {
                    "value": 24,
                    "label": "驻马店市分公司"
                }
            ],
            "key": "subordinate_department_computerroom",
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "select"
        },
        {
            "inputType": "select",
            "label": "建设规划所属部室",
            "options": [
                {
                    "value": 0,
                    "label": "部室"
                }
            ],
            "key": "construction_planning_responsible_unit",
            "validators": [
                {
                    "label": "required"
                }
            ]
        },
        {
            "validators": [
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "person_in_charge_construction",
            "label": "建设规划责任人"
        },
        {
            "validators": [
                {
                    "value": "^(1)\\d{10}$",
                    "label": "customReg"
                },
                {
                    "label": "required"
                }
            ],
            "inputType": "input",
            "key": "subordinate_department_construction",
            "label": "建设规划责任人联系方式"
        }
    ]
    subordinate_department_system_index, subordinate_department_system = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "系统维护所属单位" else None for item in a]
    )).__getitem__(0)
    responsible_department_index, _ = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "系统维护所属部室" else None for item in a]
    )).__getitem__(0)

    # if subordinate_department_system_index > responsible_department_index:
    #     a.insert(responsible_department_index - 1, subordinate_department_system)
    #     a.pop(subordinate_department_system_index)
    # else:
    #     a.pop(subordinate_department_system_index)
    #     a.insert(responsible_department_index - 1, subordinate_department_system)
    a.pop(subordinate_department_system_index)
    a.insert(responsible_department_index, subordinate_department_system)

    subordinate_department_operation_index, subordinate_department_operation = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "应用维护所属单位" else None for item in a]
    )).__getitem__(0)
    operation_maintenance_responsible_unit_index, _ = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "应用维护所属部室" else None for item in a]
    )).__getitem__(0)
    a.pop(subordinate_department_operation_index)
    a.insert(operation_maintenance_responsible_unit_index, subordinate_department_operation)

    subordinate_department_use_index, subordinate_department_use = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "运营使用所属单位" else None for item in a]
    )).__getitem__(0)
    use_maintenance_responsible_unit_index, _ = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "运营使用所属部室" else None for item in a]
    )).__getitem__(0)
    a.pop(subordinate_department_use_index)
    a.insert(use_maintenance_responsible_unit_index, subordinate_department_use)

    subordinate_department_hardware_index, subordinate_department_hardware = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "硬件维护所属单位" else None for item in a]
    )).__getitem__(0)
    hardware_maintenance_responsible_unit_index, _ = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "硬件维护所属部室" else None for item in a]
    )).__getitem__(0)
    a.pop(subordinate_department_hardware_index)
    a.insert(hardware_maintenance_responsible_unit_index, subordinate_department_hardware)

    subordinate_department_computerroom_index, subordinate_department_computerroom = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "机房管理所属单位" else None for item in a]
    )).__getitem__(0)
    computerroom_management_responsible_unit, _ = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "机房管理所属部室" else None for item in a]
    )).__getitem__(0)
    a.pop(subordinate_department_computerroom_index)
    a.insert(computerroom_management_responsible_unit, subordinate_department_computerroom)

    subordinate_department_equipment_index, subordinate_department_equipment = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "建设规划所属单位" else None for item in a]
    )).__getitem__(0)
    construction_planning_responsible_unit_index, construction_planning_responsible_unit = list(filter(
        lambda x: x,
        [(a.index(item), item) if str(item.get("label")) == "建设规划所属部室" else None for item in a]
    )).__getitem__(0)
    a.pop(subordinate_department_equipment_index)
    a.insert(construction_planning_responsible_unit_index, subordinate_department_equipment)

    for ii, i in enumerate(a, start=1):
        print(ii, i.get("label"))


def test_03():
    query_organization_all_list_sql = (
        "select internal_app_permission.tb_user_group.id::int, "
        "internal_app_permission.tb_user_group.name::varchar "
        "from internal_app_permission.tb_user_group "
        "inner join internal_app_permission.tb_user_group_tree "
        "on internal_app_permission.tb_user_group_tree.user_group_id = internal_app_permission.tb_user_group.id "
        "inner join (select internal_app_permission.tb_user_group.id "
        "from internal_app_permission.tb_user_group "
        "where internal_app_permission.tb_user_group.name = '全流量资产管理系统') as temp "
        "on temp.id = internal_app_permission.tb_user_group_tree.parent_id;"
    )

    print(query_organization_all_list_sql)


class StaticClass(object):

    @staticmethod
    def __str__():
        return "StaticClass ..."


def test_04():
    l = ["全流量资产管理系统", "测试机构1"]
    l = list(filter(lambda x: not str(x).__eq__("全流量资产管理系统"), l))
    print(l)


if __name__ == '__main__':
    # test_02()
    # test_03()
    # print(StaticClass.__str__())
    test_04()
