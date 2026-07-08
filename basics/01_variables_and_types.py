"""
01 - 变量与数据类型（对比 Java）

== Python 与 Java 在变量上的关键差异 ==
1. Python 是动态类型语言，变量本身没有类型，只有"值"有类型。
   同一个变量可以先后指向不同类型的对象（不推荐这样做）。
2. Python 不需要分号；没有大括号 {}，用缩进（4 空格）表示代码块。
3. Python 用 snake_case 命名变量和函数；类名用 PascalCase；
   常量用全大写 + 下划线（这只是约定，没有真正的常量）。
4. 字符串可以用单引号 ' '、双引号 " "、三引号 ''' ''' 或 """ """。
   f-string（格式化字符串）相当于 Java 17+ 的 STR."{}" 模板字符串。
5. Python 的 None 相当于 Java 的 null（关键字首字母大写）。
"""

# ============================================================
# 1. 变量赋值
# ============================================================
# Java 中需要写：int num = 5;
# Python 中：直接赋值即可，无需声明类型
num = 5  # num 现在指向一个 int 对象
num_str = "5"  # 可以立刻换成字符串
print("num =", num, "type =", type(num))  # type() 用来查看类型，相当于 Java 的 getClass()
print("num_str =", num_str, "type =", type(num_str))

# Python 中所有的赋值都是"把名字绑定到对象上"
# 这点和 Java 的"基本类型存值、引用类型存地址"略有差异
a = [1, 2, 3]
b = a  # b 和 a 指向同一个 list 对象
b.append(4)
print("a =", a)  # a 也会变成 [1, 2, 3, 4] —— 引用语义，类似 Java 的引用类型
# 如果想要"复制一份"，需要显式调用 .copy() 或使用 copy 模块
c = a.copy()
c.append(5)
print("a =", a, "c =", c)  # a 不受影响，c 是独立的新对象

# ============================================================
# 2. 基本数据类型
# ============================================================
# 常用的"标量"类型对照：
#   Python        Java
#   ----------    --------------
#   int           long（无大小限制，非常方便）
#   float         double
#   bool          boolean（注意：True/False 首字母大写）
#   str           String
#   NoneType      void / null

big_number = 10 ** 100  # Python 的 int 理论上没有上限
print("\nbig_number =", big_number)

pi = 3.14159
is_python_fun = True  # 注意首字母大写，不能写 true
nothing = None  # 类似 Java 的 null，但 None 是关键字

print(f"pi={pi}, is_python_fun={is_python_fun}, nothing={nothing}")

# ============================================================
# 3. 字符串
# ============================================================
name = "zhangweipeng"
greeting = "Hello, " + name  # 字符串拼接，等价于 Java 的 +
repeated = "ha" * 3  # 重复：等价于 "ha".repeat(3)
print("\n字符串：")
print("greeting =", greeting)
print("repeated =", repeated)

# 切片（slice）：Python 独有的"取子串"方式
#   s[start:stop:step]，左闭右开
print("name[0:5] =", name[0:5])  # 前 5 个字符
print("name[::-1] =", name[::-1])  # 反转字符串
print("name.upper() =", name.upper())  # 转大写

# f-string：Python 3.6+ 推荐的字符串格式化方式
# Java 对应：String.format("Hello, %s", name) 或 STR."Hello, \{name}"
age = 30
print(f"我叫 {name}, 今年 {age} 岁, 明年 {age + 1} 岁")

# 一些常用方法
s = "  python learning  "
print(f"strip='{s.strip()}', len={len(s)}, startswith='{s.strip().startswith('py')}'")


# ============================================================
# 4. 类型提示（Type Hints）—— 让 Python 拥有"类 Java"的类型体验
# ============================================================
# Python 3.5+ 引入类型提示，仅作为提示，运行时不会强制检查
# Java 风格的写法：
#   int total(int a, int b) { return a + b; }
# Python 等价：
def total(a: int, b: int) -> int:
    """两数相加，带类型提示"""
    return a + b


print("\n带类型提示的函数：total(3, 5) =", total(3, 5))

# 可以使用 typing 模块表达更复杂的类型
# Python 3.9+ 可以直接使用 list[str]、dict[str, int]，旧版本需要 from typing import List, Dict
from typing import Optional


def find_user(user_id: int) -> Optional[str]:  # Optional[str] ≈ @Nullable String
    """模拟根据 id 查用户名"""
    if user_id == 1:
        return "alice"
    return None  # 用 None 表示"没有"，类似 Java 的 return null


# ============================================================
# 5. 多重赋值与解包
# ============================================================
# Java 没有直接对应的语法，但可以理解为"一次性声明多个变量"
x, y, z = 1, 2, 3
print("\n多重赋值：x, y, z =", x, y, z)

# 交换两个变量：Python 一行搞定
x, y = y, x
print("交换后：x =", x, "y =", y)

# ============================================================
# 小结
# ============================================================
# - 动态类型：不需要写类型，但要养成"心里有数"的习惯
# - 强烈建议开启 IDE/编辑器的类型检查（mypy、pyright）以获得接近 Java 的体验
# - f-string 是格式化字符串的首选
# - None 替代 null，首字母大写
