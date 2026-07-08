"""
06 - 异常处理（对比 Java try-catch）

== Python 与 Java 在异常上的关键差异 ==
1. 用 try / except / finally / else（Java 没有 else 分支）。
2. 没有"受检异常"（checked exception），所有异常都是非受检的。
   不需要在方法签名上 throws XxxException。
3. 可以一次捕获多个异常：except (TypeError, ValueError) as e:
4. 主动抛异常用 raise 关键字（Java 是 throw）。
5. 可以重新抛出当前异常：raise（不带参数）。
6. 推荐使用 with 语句管理资源（等价于 Java 的 try-with-resources）。
"""

# ============================================================
# 1. 基本的 try / except
# ============================================================
# Java：
#   try {
#       int n = Integer.parseInt(s);
#   } catch (NumberFormatException e) {
#       ...
#   }
# Python：
print("=== 基本异常处理 ===")


def to_int(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:  # as e 拿到异常对象
        print(f"  转换失败: {e!r}")
        return 0
    else:
        # 当且仅当 try 块没有抛异常时执行
        print("  转换成功")
    finally:
        # 无论是否异常都执行，类似 Java 的 finally
        print("  finally 始终执行")


print(to_int("123"))
print(to_int("abc"))

# ============================================================
# 2. 同时捕获多个异常
# ============================================================
print("\n=== 同时捕获多个异常 ===")


def safe_div(a: str, b: str) -> float:
    try:
        return float(a) / float(b)
    except (ValueError, TypeError) as e:
        print(f"  参数类型错误: {e!r}")
        return 0.0
    except ZeroDivisionError as e:
        print(f"  除数不能为零: {e!r}")
        return 0.0


print("safe_div('10', '2') =", safe_div("10", "2"))
print("safe_div('10', '0') =", safe_div("10", "0"))
print("safe_div('abc', '2') =", safe_div("abc", "2"))

# ============================================================
# 3. 主动抛异常
# ============================================================
print("\n=== raise 抛异常 ===")


class InsufficientFundsError(Exception):
    """自定义异常（继承 Exception）"""

    def __init__(self, balance: float, amount: float):
        super().__init__(f"余额 {balance} 不足以支付 {amount}")
        self.balance = balance
        self.amount = amount


def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(f"  异常: {e}")

# ============================================================
# 4. 重新抛出当前异常
# ============================================================
print("\n=== 重新抛出 ===")


def process():
    try:
        int("abc")
    except ValueError:
        print("  在 process 中记录日志")
        raise  # 重新抛出当前异常，相当于 Java 的 throw;


try:
    process()
except ValueError as e:
    print(f"  外层捕获: {e!r}")

# ============================================================
# 5. with 语句 —— 资源管理（对比 try-with-resources）
# ============================================================
print("\n=== with 语句管理资源 ===")


# Java 7+ 的 try-with-resources：
#   try (BufferedReader br = new BufferedReader(new FileReader("x.txt"))) {
#       return br.readLine();
#   }
# Python 用 with：
#   with open("x.txt") as f:
#       return f.readline()
#
# with 后面跟的对象只要实现了 __enter__ 和 __exit__ 协议即可

# 自定义支持 with 的类
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"  耗时: {self.elapsed * 1000:.3f} ms")
        return False  # False 表示不吞掉异常


with Timer():
    total = sum(range(1, 10000))
    print(f"  sum = {total}")

# ============================================================
# 6. 异常的层级
# ============================================================
# Python 内建异常的主要层级（Java 是单一的 Throwable 层级）：
#   BaseException
#   ├── KeyboardInterrupt   (Ctrl+C)
#   ├── SystemExit          (sys.exit)
#   └── Exception
#       ├── ValueError
#       ├── TypeError
#       ├── IndexError
#       ├── KeyError
#       ├── FileNotFoundError
#       ├── ZeroDivisionError
#       └── ...
#
# 捕获时建议尽量精确，避免直接 except Exception（会吞掉 KeyboardInterrupt 等）


# ============================================================
# 小结
# ============================================================
# - try / except / else / finally 四件套
# - 自定义异常继承 Exception
# - 资源管理优先用 with 语句
