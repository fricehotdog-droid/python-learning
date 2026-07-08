"""
04 - 函数（对比 Java 方法）

== Python 与 Java 在函数上的关键差异 ==
1. 用 def 关键字定义函数；def 后面是函数名和参数列表。
2. 没有访问修饰符（public/private）；以下划线开头表示"内部使用"（约定）。
3. 没有重载（overload）：同名函数只能定义一次。
   可以用 *args / **kwargs 模拟"可变参数"，或用 default 参数实现"重载"。
4. 支持默认参数值、关键字参数、任意数量的位置/关键字参数。
5. 函数是一等公民（first-class）：可以赋值给变量、作为参数传递、作为返回值。
6. 匿名函数用 lambda 关键字；类似 Java 的 (a, b) -> a + b。
7. 没有 void 关键字：没写 return 等价于 return None。
"""


# ============================================================
# 1. 基本定义
# ============================================================
# Java：
#   public int add(int a, int b) { return a + b; }
# Python：
def add(a: int, b: int) -> int:
    """两数相加的简短说明。文档字符串（docstring）可用 help() 查看。"""
    return a + b

print("=== 基本函数 ===")
print("add(3, 5) =", add(3, 5))


# ============================================================
# 2. 默认参数 & 关键字参数
# ============================================================
def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    return f"{greeting}, {name}{punctuation}"

print("\n=== 默认参数 ===")
print(greet("Alice"))                            # 使用默认值
print(greet("Bob", "Hi"))                         # 位置参数
print(greet("Carol", punctuation="."))            # 关键字参数
print(greet("Dave", greeting="Hey", punctuation="?"))   # 同时使用多个关键字参数
# greet(name="Eve", "Hello")                     # ❌ 语法错误：位置参数必须在关键字参数之前


# ============================================================
# 3. *args / **kwargs —— 任意数量的参数
# ============================================================
# Java 需要用 varargs (String... args) + Map<String, Object> 来模拟
def log(level: str, *messages: str, **context: object) -> None:
    """可变位置参数 + 可变关键字参数"""
    print(f"[{level}]", " ".join(messages), "|", context)

print("\n=== *args / **kwargs ===")
log("INFO", "user", "logged", "in", user_id=1, ip="127.0.0.1")


# ============================================================
# 4. 一等公民：函数作为参数 / 返回值
# ============================================================
print("\n=== 函数是一等公民 ===")
def apply(value: int, func) -> int:    # func 没有类型提示，演示动态类型
    return func(value)

print("apply(5, lambda x: x * 2) =", apply(5, lambda x: x * 2))
print("apply(5, lambda x: x ** 2) =", apply(5, lambda x: x ** 2))

# 高阶函数：返回函数
def make_multiplier(factor: int):
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print("double(5) =", double(5), "triple(5) =", triple(5))


# ============================================================
# 5. lambda 表达式
# ============================================================
print("\n=== lambda ===")
# Java: (a, b) -> a + b
# Python: lambda a, b: a + b
adder = lambda a, b: a + b
print("adder(3, 4) =", adder(3, 4))

# 常用于排序、过滤等场景
items = [(1, "b"), (2, "a"), (3, "c")]
items.sort(key=lambda x: x[1])   # 按第二个元素排序
print("按字母排序:", items)


# ============================================================
# 6. 作用域与闭包
# ============================================================
print("\n=== 作用域与闭包 ===")
message = "global"           # 全局变量

def outer():
    message = "enclosing"     # 闭包变量
    def inner():
        # nonlocal message   # 如果要修改闭包变量，需要加 nonlocal
        return message        # 读取没问题
    return inner

print("outer()() =", outer()())   # 仍然是 "enclosing"

# LEGB 规则：Local → Enclosing → Global → Built-in
# 类似于 Java 的"就近原则"，但作用域规则比 Java 更明确


# ============================================================
# 7. 参数解包（Unpacking）
# ============================================================
print("\n=== 参数解包 ===")
def show(a, b, c):
    print(f"a={a}, b={b}, c={c}")

args = [1, 2, 3]
show(*args)                   # 相当于 show(1, 2, 3)

kwargs = {"a": 1, "b": 2, "c": 3}
show(**kwargs)                # 相当于 show(a=1, b=2, c=3)


# ============================================================
# 小结
# ============================================================
# - 默认参数一定要用不可变对象（int/str/tuple/None），否则会产生"陷阱"
# - lambda 适合短小函数；复杂逻辑请用 def
# - 函数是一等公民是 Python 函数式特性的基础（map/filter/reduce、装饰器等）
