"""
08 - 模块、常用内建、装饰器入门（对比 Java import / 工具类 / 注解）

== 本节内容 ==
1. 模块与包：import 的多种写法
2. 常用内建函数：map / filter / any / all / zip / enumerate 等
3. 常用标准库：datetime / os / sys / re / collections 简介
4. 装饰器入门：@ 语法糖（对比 Java 注解 + AOP）
"""

# ============================================================
# 1. 模块与包
# ============================================================
# Java 中我们写 import java.util.List;
# Python 中写：
#   import os                        # 导入整个模块
#   from os import path              # 从模块中导入某个名字
#   from os import path as p         # 起别名
#   from os import *                 # 不推荐，会污染命名空间

print("=== 模块与包 ===")
import math
from math import sqrt, pi
import datetime as dt

print("math.sqrt(16) =", math.sqrt(16))  # 4.0
print("sqrt(25) =", sqrt(25))  # 5.0（直接使用名字）
print("pi =", pi)

now = dt.datetime.now()
print("当前时间 =", now)

# ============================================================
# 2. 常用内建函数
# ============================================================
print("\n=== map / filter / any / all / zip ===")
nums = [1, 2, 3, 4, 5]

# map: 把函数应用到每个元素（Java 8+ 的 stream().map(...)）
squared = list(map(lambda x: x * x, nums))
print("map ->", squared)

# filter: 过滤（Java 的 stream().filter(...)）
evens = list(filter(lambda x: x % 2 == 0, nums))
print("filter ->", evens)

# any / all: 短路逻辑
print("any > 4:", any(x > 4 for x in nums))  # 至少一个 > 4
print("all > 0:", all(x > 0 for x in nums))  # 全部 > 0

# zip: 把多个可迭代对象"拉链"到一起
a = [1, 2, 3]
b = ["a", "b", "c"]
print("zip:", list(zip(a, b)))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# ============================================================
# 3. 常用标准库一览
# ============================================================
print("\n=== 常用标准库 ===")
# datetime —— 日期时间
now = dt.datetime.now()
print("now =", now, "iso =", now.isoformat())

# os —— 操作系统交互
import os

print("cwd =", os.getcwd())  # 当前工作目录
print("env PATH 存在?", "PATH" in os.environ)

# sys —— Python 解释器
import sys

print("Python 版本 =", sys.version.split()[0])
print("平台 =", sys.platform)

# collections —— 扩展容器
from collections import Counter, defaultdict, namedtuple

# Counter：词频统计（类似 Java 的 Multiset / Stream groupingBy）
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print("Counter =", counter)
print("most_common(1) =", counter.most_common(1))

# defaultdict：带默认值的 dict
dd: defaultdict[str, list[str]] = defaultdict(list)
dd["fruits"].append("apple")
print("defaultdict =", dict(dd))

# namedtuple：带字段名的 tuple（类似 Java record）
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print("Point =", p, "x =", p.x)

# ============================================================
# 4. 装饰器（Decorator）入门
# ============================================================
# 装饰器 = "把一个函数包一层"，常用于日志、计时、权限校验等横切关注点
# 类似于 Java 的"自定义注解 + AOP 切面"
print("\n=== 装饰器 ===")

# 4.1 函数装饰器
import functools
import time


def timer(func):
    """打印函数执行时间的装饰器"""

    @functools.wraps(func)  # 保留原函数的 __name__、__doc__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  [{func.__name__}] 耗时 {elapsed:.3f} ms")
        return result

    return wrapper


@timer
def slow_sum(n: int) -> int:
    """计算 1..n 的和"""
    return sum(range(1, n + 1))


slow_sum(100000)


# 4.2 带参数的装饰器
def repeat(times: int):
    """把函数调用 times 次"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return decorator


@repeat(3)
def greet(name: str) -> str:
    return f"Hi, {name}!"


print("greet('Alice') =", greet("Alice"))


# 4.3 类装饰器：让类实例可以像函数一样被调用
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"  第 {self.count} 次调用 {self.func.__name__}")
        return self.func(*args, **kwargs)


@CountCalls
def hello():
    print("  hello!")


hello()
hello()
hello()

# ============================================================
# 5. 虚拟环境与依赖（针对本项目）
# ============================================================
# 本项目使用 uv 作为包管理工具（一个用 Rust 写的、非常快的 pip/poetry 替代品）
#
# 常用命令（推荐记下来）：
#   uv venv                 创建虚拟环境（项目里已经创建过 .venv）
#   uv add <package>        添加依赖，会自动改 pyproject.toml + uv.lock
#   uv remove <package>     移除依赖
#   uv run python main.py   在虚拟环境中执行命令
#   uv sync                 按 lock 文件同步依赖
#   uv pip list             查看已安装的包
#
# 与 Java 的 Maven/Gradle 对比：
#   pyproject.toml    ≈  pom.xml / build.gradle
#   uv.lock           ≈  Maven 的 dependency lock 或 Gradle 的 lockfile
#   .venv             ≈  本地的 Maven 仓库 + 编译输出


# ============================================================
# 小结
# ============================================================
# - import 是 Python 复用代码的核心
# - map/filter/any/all/zip 在数据处理时非常好用
# - 装饰器是 Python 的"招牌特性"，能优雅地实现 AOP
# - 本项目用 uv 管理依赖，运行命令请用 uv run python xxx.py
