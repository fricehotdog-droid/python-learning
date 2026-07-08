"""
05 - 类与面向对象（对比 Java class）

== Python 与 Java 在 OOP 上的关键差异 ==
1. 类的定义用 class 关键字；类体同样靠缩进。
2. 一切皆对象：class 本身、函数、int 都是对象。
3. 没有 public / private / protected 修饰符：
   - 默认公开
   - 单下划线 _name 表示"内部使用"（约定）
   - 双下划线 __name 会触发名称改写（name mangling），更难被子类覆盖
4. 没有接口（interface），用"鸭子类型"或抽象基类（abc.ABC）替代。
5. 继承语法：class Sub(Base):
6. 构造函数：__init__（不是类名）
7. self 相当于 Java 的 this，但必须显式作为第一个参数。
8. 多继承是允许的（用 MRO 解决菱形问题）。
"""


# ============================================================
# 1. 基本类
# ============================================================
class Dog:
    """一个简单的 Dog 类"""
    # 类属性：所有实例共享
    species = "Canis familiaris"

    # 构造方法：相当于 Java 的构造器
    def __init__(self, name: str, age: int):
        # 实例属性：每个实例独立
        self.name = name
        self.age = age

    # 实例方法：第一个参数必须是 self
    def bark(self) -> str:
        return f"{self.name}: 汪汪！"

    # 相当于 Java 的 toString()
    def __str__(self) -> str:
        return f"Dog(name={self.name}, age={self.age})"

    # 相当于 Java 的 equals()
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dog):
            return False
        return self.name == other.name and self.age == other.age

    # 类的"一般方法"（不依赖 self/cls），相当于 Java 的 static 方法
    @staticmethod
    def info() -> str:
        return "Dog 是人类的好朋友"

    # 替代 Java 的 getter（@property 把方法伪装成属性）
    @property
    def human_age(self) -> int:
        """狗的年龄换算成人类年龄（粗略）"""
        return self.age * 7


print("=== 基本类 ===")
dog = Dog("旺财", 3)
print(dog.species)
print(dog)  # 走 __str__
print(dog.bark())
print("人类年龄 =", dog.human_age)  # 像访问属性一样调用方法
print(Dog.info())


# ============================================================
# 2. 继承
# ============================================================
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."


class Cat(Animal):
    def __init__(self, name: str, color: str):
        # 调用父类构造器：相当于 Java 的 super(name)
        super().__init__(name)
        self.color = color

    # 方法重写
    def speak(self) -> str:
        return f"{self.name}: 喵~"

    def __str__(self) -> str:
        return f"Cat(name={self.name}, color={self.color})"


print("\n=== 继承 ===")
cat = Cat("小花", "白色")
print(cat)
print(cat.speak())
print("isinstance(cat, Animal) =", isinstance(cat, Animal))  # 替代 instanceof
print("isinstance(cat, Dog) =", isinstance(cat, Dog))


# ============================================================
# 3. 访问控制（下划线约定）
# ============================================================
class Account:
    def __init__(self, owner: str, balance: float):
        self.owner = owner  # 公开
        self._balance = balance  # 约定：内部使用（单下划线）
        self.__secret = "haha"  # 名称改写，双下划线开头 → _Account__secret

    def get_balance(self) -> float:
        return self._balance


print("\n=== 访问控制 ===")
acc = Account("Alice", 1000)
print("owner =", acc.owner)  # OK
print("balance =", acc._balance)  # 能访问，但约定不要
print("get_balance =", acc.get_balance())
# print(acc.__secret)                      # ❌ AttributeError
# 实际名称已被改写：
print("name mangled ->", acc._Account__secret)


# ============================================================
# 4. 多继承 & MRO
# ============================================================
class A:
    def hello(self) -> str:
        return "A.hello"


class B(A):
    def hello(self) -> str:
        return "B.hello"


class C(A):
    def hello(self) -> str:
        return "C.hello"


# Python 用 C3 线性化算法确定 MRO（方法解析顺序）
class D(B, C):
    pass


print("\n=== 多继承 ===")
d = D()
print("d.hello() =", d.hello())  # B 在前，调用 B 的 hello
print("D.__mro__ =", D.__mro__)  # 打印方法解析顺序

# ============================================================
# 5. 抽象基类（替代 Java 的 interface / abstract class）
# ============================================================
from abc import ABC, abstractmethod


class Shape(ABC):  # 继承 ABC 表示这是抽象类
    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimeter(self) -> float:
        ...


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


print("\n=== 抽象基类 ===")
rect = Rectangle(3, 4)
print("面积 =", rect.area())
# shape = Shape()                       # ❌ TypeError: 不能实例化抽象类


# ============================================================
# 6. 数据类（Data Class）—— 替代 Java 的 record / Lombok @Data
# ============================================================
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"  # 可以有默认值


print("\n=== 数据类 ===")
p1 = Point(1, 2)
p2 = Point(1, 2, "p2")
print("p1 =", p1)  # 自动 __repr__
print("p1 == p2:", p1 == Point(1, 2))  # 自动 __eq__

# ============================================================
# 小结
# ============================================================
# - self 是显式的；下划线代替访问修饰符
# - 数据类（@dataclass）非常实用，类似 Java record
# - 多继承能不用就不用；优先用组合（has-a）或抽象基类
