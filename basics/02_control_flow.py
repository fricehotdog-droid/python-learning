"""
02 - 控制流：if / for / while / match（对比 Java）

== Python 与 Java 在控制流上的关键差异 ==
1. 没有大括号 {}，靠缩进表示代码块（4 空格或 1 个 tab，绝不能混用）。
2. 条件表达式不需要括号：if x > 0: 而不是 if (x > 0) { ... }。
3. 没有 else if，写成 elif。
4. 没有 i++，自增/自减写成 i += 1。
5. for 循环默认遍历"可迭代对象"，不需要写索引（类似 Java 的 for-each）。
6. Python 3.10+ 引入了 match-case，对应 Java 的 switch 表达式（更强大）。
"""


# ============================================================
# 1. if / elif / else
# ============================================================
# Java 写法：
#   if (score >= 90) { grade = "A"; }
#   else if (score >= 80) { grade = "B"; }
#   else { grade = "C"; }
#
# Python 写法：
def grade_of(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:  # 注意是 elif，不是 else if
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


print("=== if/elif/else ===")
print("95 ->", grade_of(95))
print("72 ->", grade_of(72))

# 简洁写法：三元表达式（类似 Java 的 condition ? a : b）
status = "及格" if grade_of(75) in ("A", "B", "C") else "不及格"
print("三元表达式 status =", status)

# ============================================================
# 2. 真值判断（Truthiness）
# ============================================================
# Python 中以下值被视为"假"（Falsy），其余都是"真"：
#   False, None, 0, 0.0, "", [], {}, set()
# Java 中只能写 if (list != null && !list.isEmpty())，Python 直接写 if not list:
print("\n=== 真值判断 ===")
items = []
if not items:  # 替代 Java 的 list == null || list.isEmpty()
    print("items 为空")
items.append("x")
if items:
    print("items 不为空，长度 =", len(items))

# ============================================================
# 3. for 循环
# ============================================================
print("\n=== for 循环 ===")

# 3.1 遍历集合（类似 Java 的 for (String s : list)）
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("fruit =", fruit)

# 3.2 带索引遍历：用 enumerate 替代 Java 的 for (int i = 0; i < list.size(); i++)
print("\n带索引遍历：")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")
print()
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

# 3.3 range：Python 替代 Java 的 for (int i = 0; i < n; i++)
#   range(stop)：0..stop-1
#   range(start, stop)：start..stop-1
#   range(start, stop, step)：按步长
print("\nrange(5)：")
for i in range(5):
    print("  i =", i)

# 3.4 同时遍历多个集合：zip
names = ["Alice", "Bob", "Charlie"]
scores = [95, 82, 76]
print("\nzip 同时遍历多个集合：")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# ============================================================
# 4. while 循环
# ============================================================
print("\n=== while 循环 ===")
n = 5
while n > 0:
    print("n =", n)
    n -= 1  # 没有 n-- 这种写法
else:
    # while 后面的 else：循环正常结束（没被 break）时执行
    # Java 没有这个特性
    print("循环正常结束")

# break / continue 用法与 Java 完全一致


# ============================================================
# 5. match-case（Python 3.10+，对应 Java 的 switch 表达式）
# ============================================================
print("\n=== match-case ===")


def describe(point: tuple[int, int]) -> str:
    match point:
        case (0, 0):
            return "原点"
        case (0, y):
            return f"在 y 轴上, y={y}"
        case (x, 0):
            return f"在 x 轴上, x={x}"
        case (x, y) if x == y:  # 带守卫条件
            return f"在 y=x 直线上, ({x}, {y})"
        case (x, y):  # 任意匹配，类似 Java 的 default
            return f"普通点 ({x}, {y})"


print(describe((0, 0)))
print(describe((0, 5)))
print(describe((3, 0)))
print(describe((7, 7)))
print(describe((1, 2)))

# ============================================================
# 小结
# ============================================================
# - 缩进就是语法，写错会直接 IndentationError
# - for 循环优先用 for-in + enumerate/zip，而不是手写索引
# - match-case 比 switch 强大，可以解构 tuple/list/对象
# - 没有 i++，要写 i += 1
