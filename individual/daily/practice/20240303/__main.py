# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 03, 2024
"""


class Singleton:

    def __init__(self, __method):
        self.__method = __method
        self.__instance = {}

    def __call__(self, *args, **kwargs):
        if not self.__instance:
            self.__instance.update(__instance=self.__method(*args, **kwargs))
            return self.__instance.get("__instance")
        else:
            return self.__instance.get("__instance")


@Singleton
class Person:

    def __init__(self, a, b=1):
        self.a = a
        self.b = b

    def print_a(self):
        print(self.a)

    def print_b(self):
        print(self.b)


class Test:

    @classmethod
    def run(cls):
        expressions = [
            "计数+三级数量*二级标准工时",
            "(计数 + 三级数量) * 二级标准工时",
            "三级数量 - 2 * 计数",
            "三级标准工时 / 二级数量 - 计数 * 2",
            "计数 + (三级数量 + 二级数量) * 二级标准工时",
            "计数 - 三级数量 + 二级标准工时",
            "三级数量 * 二级数量 - 二级标准工时 / 计数",
            "2 * 计数 + 三级标准工时",
            "计数 * (三级数量 + 二级数量) - 二级标准工时",
            "三级数量 + 二级数量 * (二级标准工时 / 计数)",
            "计数 + 三级数量 * 二级标准工时 - 二级数量",
            "计数 * (三级数量 - 二级数量) / 二级标准工时",
            "2 * (三级数量 + 计数) * 二级标准工时",
            "计数 + 三级数量 * 二级标准工时 - (二级数量 / 2)",
            "计数 + 三级数量 * (二级标准工时 - 二级数量)",
            "三级数量 + (二级数量 * 计数) / 二级标准工时",
            "计数 + 三级数量 * 二级标准工时 / (二级数量 - 1)",
            "2 * (三级数量 + (计数 - 二级数量)) * 二级标准工时",
            "2 * (三级数量 + (计数 - 二级数量)) * 二级标准工时)",
            "2 * (三级数量 + (计数 - 二级数量))",
            "2 * 三级数量 + (计数 - 二级数量) * 二级标准工时 +"
        ]
        for expression in expressions:
            print(cls.test_1(expression))

    @staticmethod
    def test_1(expression):
        replaced_expression = expression.replace("计数", "1").replace("三级数量", "1").replace("二级标准工时", "1").replace("二级数量", "1").replace("三级标准工时", "1")
        try:
            eval(replaced_expression)
            return True
        except ZeroDivisionError:
            return True
        except Exception:
            return False


if __name__ == '__main__':
    Test.run()
