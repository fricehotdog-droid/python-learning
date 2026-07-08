"""
03 - 数据结构：list / tuple / set / dict（对比 Java 集合）

== Python 与 Java 在集合上的关键差异 ==
1. Python 的"内置容器"已经非常强大，绝大多数场景不需要引第三方库。
2. 常用 4 个：
     list    —— 有序、可变、可重复    ≈  Java 的 ArrayList
     tuple   —— 有序、不可变          ≈  Java 的 record / 不可变 List
     set     —— 无序、不可重复        ≈  Java 的 HashSet
     dict    —— 键值对               ≈  Java 的 HashMap
3. 容器内可以放任意类型（Python 不会做泛型检查），但建议保持单一类型。
4. 一切皆对象，list / dict 本身也是对象，可以调用大量方法。
5. 列表推导式 [x*2 for x in xs] ≈ Java 8+ 的 list.stream().map(...).toList()。
"""

# ============================================================
# 1. list —— 有序可变序列
# ============================================================
print("=== list（≈ ArrayList）===")
nums = [1, 2, 3, 4, 5]
nums.append(6)  # 末尾追加 ≈ list.add(e)
nums.insert(0, 0)  # 在指定位置插入 ≈ list.add(0, e)
nums.extend([7, 8])  # 合并另一个 list ≈ list.addAll(other)
nums.remove(3)  # 删除第一个匹配的元素
print("nums =", nums)
print("len(nums) =", len(nums))  # 类似 list.size()
print("nums[0] =", nums[0], "nums[-1] =", nums[-1])  # 负数索引从末尾开始

# 切片
print("nums[1:4] =", nums[1:4])  # [2, 4, 5]
print("nums[::-1] =", nums[::-1])  # 反转

# 排序：nums.sort() 原地排序；sorted(nums) 返回新列表
nums.sort(reverse=True)
print("降序 nums =", nums)

# ============================================================
# 2. tuple —— 有序不可变
# ============================================================
print("\n=== tuple（≈ 不可变 List）===")
point = (3, 5)
x, y = point  # 解包：类似 Java 的 record 解构 (Java 21+)
print(f"x={x}, y={y}")

# 不可变：point[0] = 10 会抛 TypeError
# 常用于"函数返回多个值"或"作为 dict 的 key"
RGB = {
    (255, 0, 0): "red",
    (0, 255, 0): "green",
    (0, 0, 255): "blue",
}
print("RGB[(255,0,0)] =", RGB[(255, 0, 0)])

# ============================================================
# 3. set —— 无序不可重复
# ============================================================
print("\n=== set（≈ HashSet）===")
a = {1, 2, 3, 3, 3}
print("a =", a)  # 自动去重：{1, 2, 3}

b = {3, 4, 5}
print("a & b (交集) =", a & b)  # 类似 a.retainAll(b)
print("a | b (并集) =", a | b)  # 类似 addAll
print("a - b (差集) =", a - b)  # 类似 removeAll
print("a ^ b (对称差) =", a ^ b)  # 异或

# 集合推导式
squares = {x * x for x in range(5)}
print("squares =", squares)

# ============================================================
# 4. dict —— 键值对
# ============================================================
print("\n=== dict（≈ HashMap）===")
user = {"name": "Alice", "age": 30, "city": "Beijing"}
print("user =", user)
print("user['name'] =", user["name"])
print("user.get('email', 'N/A') =", user.get("email", "N/A"))  # get 带默认值 ≈ Map.getOrDefault

user["email"] = "alice@example.com"  # 新增 / 修改
user.setdefault("phone", "13800000000")  # 存在则忽略，不存在则插入
print("after setdefault:", user)

# 遍历
for key, value in user.items():  # 类似 user.forEach((k, v) -> ...)
    print(f"  {key} = {value}")

# 字典推导式
square_map = {x: x * x for x in range(5)}
print("square_map =", square_map)

# 合并字典（Python 3.9+）
defaults = {"theme": "dark", "lang": "en"}
overrides = {"lang": "zh-CN"}
config = defaults | overrides
print("merged config =", config)

# ============================================================
# 5. 列表推导式（List Comprehension）—— Python 的"招牌特性"
# ============================================================
print("\n=== 列表推导式 ===")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 取偶数
evens = [n for n in nums if n % 2 == 0]
# Java 等价：
#   List<Integer> evens = nums.stream().filter(n -> n % 2 == 0).toList();
print("evens =", evens)

# 把每个元素平方
squares_list = [n * n for n in nums]
print("squares_list =", squares_list)

# 二维展开
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]  # 类似 flatMap
print("flat =", flat)

# ============================================================
# 6. 一些常用内建函数
# ============================================================
print("\n=== 常用内建函数 ===")
print("sum(nums) =", sum(nums))
print("min/max =", min(nums), max(nums))
print("all/any:", all([True, True, False]), any([False, True, False]))

# enumerate：给元素加上索引
for i, v in enumerate(["a", "b", "c"]):
    print(f"  index={i}, value={v}")

# sorted：支持 key 函数，类似 Java 的 Comparator
words = ["banana", "apple", "cherry"]
print("按长度排序：", sorted(words, key=len))

# ============================================================
# 小结
# ============================================================
# - 默认用 list；需要 key-value 用 dict；需要去重用 set；不希望被修改用 tuple
# - 列表推导式可以大幅简化集合操作
# - dict.get(k, default) 比 dict[k] 更安全（key 缺失会 KeyError）
