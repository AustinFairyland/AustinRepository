def func():
    print('我是master')

name = "大佬"

print("哈哈哈哈哈哈")


# print(__name__)  # 每个模块中都会有这个内置变量
# 当此模块被直接运行的时候:  __main__   程序的入口  运行的入口
# 当这个模块被导入的时候:   master

# 以下内容: 自己运行的时候可以正常执行
# 如果被别人以模块的形式导入的时候. 不希望执行
if __name__ == '__main__':   # 被称为程序的入口
    print("以下是我的测试代码")
    print("我想给你唱首歌")
