# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-09-23 14:08:04 UTC+08:00
"""

# ==== python 3.11 ====

# 抽象基类
# 字节串
from typing import ByteString  # 字节串的抽象基类, ByteString 包括不可变的字节类, 如 bytes 和 bytearray
# 容器/序列
from typing import Container  # 容器的抽象基类, 检查对象是否包含特定元素, 实现 __contains__ 方法
from typing import Sequence  # 不可变序列的抽象基类, 如 Tuple, str
from typing import MutableSequence  # 可变序列的抽象基类, 如 List
from typing import Sized  # 一个对象是否具有确定的大小, 实现 __len__ 方法
# 字典
from typing import Mapping  # 不可变键值对对象的抽象基类, 如 Dict
from typing import MutableMapping  # 可变键值对对象的抽象基类
from typing import MappingView  # 字典视图的抽象基类
from typing import ItemsView  # 字典键值对视图的抽象基类
from typing import KeysView  # 字典键视图的抽象基类
from typing import ValuesView  # 字典值视图的抽象基类
from typing import Hashable  # 一个对象是否具有哈希值, 实现 __hash__ 方法
# 可迭代对象
from typing import Iterable  # 可迭代对象的抽象基类, 实现 __iter__ 方法
from typing import Iterator  # 迭代器的抽象基类, 实现 __iter__ 和 __next__ 方法
# 集合
from typing import MutableSet  # 可变集合的抽象基类
from typing import AbstractSet  # 不可变集合的抽象基类, 可以使用 AbstractSet 来检测对象是否实现了集合行为
# 上下文管理器
from typing import ContextManager  # 上下文管理器的抽象基类，支持 with 语句, 实现 __enter__ 和 __exit__ 方法
# 协程/异步
from typing import Awaitable  # 一个对象可以用于 await 表达式, 实现 __await__ 方法
from typing import Coroutine  # 一个协程对象, 实现 __await__ 方法
from typing import AsyncContextManager  # 一个异步上下文管理器, 实现 __aenter__ 和 __aexit__ 方法
from typing import AsyncGenerator  # 一个异步生成器对象, 实现 __aiter__ 和 __anext__ 方法
from typing import AsyncIterator  # 一个异步迭代器, 实现 __aiter__ 和 __anext__ 方法
from typing import AsyncIterable  # 一个异步可迭代对象, 实现 __aiter__ 方法

# 类型集合
from typing import ChainMap  # 一个类似字典的类, 用于创建多个字典的单一视图, 多个字典的合并视图
from typing import Counter  # 计数器
from typing import Deque  # 双端队列
from typing import Dict  # 字典
from typing import DefaultDict  # 带有默认值的字典
from typing import List  # 列表
from typing import OrderedDict  # 有序字典
from typing import Set  # 集合
from typing import FrozenSet  # 不可变集合
from typing import NamedTuple  # 工厂函数, 可以用来定义具名元组
from typing import TypedDict  # 工厂函数, 用来定义具有特定键和值类型的字典
from typing import Generator  # 生成器

# IO流
from typing import IO  # IO流, 是 BinaryIO 和 TextIO 的父类型
from typing import BinaryIO  # 二进制IO流
from typing import TextIO  # 文本IO流
# 正则
from typing import Pattern  # 编译后的正则表达式模式
from typing import Match  # 正则表达式匹配对象

# 特殊类型
from typing import Annotated  # 为类型添加元数据, Annotated[数据类型, "元数据注释1", "元数据注释2"]
from typing import Any  # 任意类型
from typing import Callable  # 可调用对象, Callable[[参数数据类型], 返回数据类型]
from typing import ClassVar  # 类变量, ClassVar[数据类型]
from typing import Concatenate  # 连接类型 (通常与 ParamSpec 一起使用)
from typing import Final  # 不可变类型, Final[数据类型]
from typing import ForwardRef  # 前向引用类型, ForwardRef["类型名称"]
from typing import Generic  # 泛型类型, Generic[类型名称]
from typing import Literal  # 字面量类型, Literal[数据1, 数据2, ...]
from typing import Optional  # 可选类型, Optional[数据类型]
from typing import ParamSpec  # 参数类型, ParamSpec[参数名称]
from typing import Protocol  # 定义结构化类型
from typing import Tuple  # 元组类型, Tuple[数据1, 数据2, ...]
from typing import Type  # 类型对象, Type[数据类型]
from typing import TypeVar  # 类型变量, TypeVar["类型名称"]
from typing import TypeVarTuple  # 类型变量元组, TypeVarTuple["类型名称1", "类型名称2", ...]
from typing import Union  # 联合类型, Union[数据类型1, 数据类型2, ...]

# 结构检查
from typing import Reversible  # 代表一个对象可以反转 reverse, 实现该协议的对象需要实现 __reversed__ 方法
from typing import SupportsAbs  # 代表一个对象可以取绝对值, 实现该协议的对象需要实现 __abs__ 方法
from typing import SupportsBytes  # 代表一个对象可以转换为字节串, 实现该协议的对象需要实现 __bytes__ 方法
from typing import SupportsComplex  # 代表一个对象可以转换为复数, 实现该协议的对象需要实现 __complex__ 方法
from typing import SupportsFloat  # 代表一个对象可以转换为浮点数, 实现该协议的对象需要实现 __float__ 方法
from typing import SupportsIndex  # 代表一个对象可以作为索引, 实现该协议的对象需要实现 __index__ 方法
from typing import SupportsInt  # 代表一个对象可以转换为整数, 实现该协议的对象需要实现 __int__ 方法
from typing import SupportsRound  # 代表一个对象可以取整, 实现该协议的对象需要实现 __round__ 方法
