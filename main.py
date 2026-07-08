"""
python-learning 总入口

目录结构：
    main.py                —— 本文件，总入口
    basics/
        01_variables_and_types.py
        02_control_flow.py
        03_data_structures.py
        04_functions.py
        05_classes.py
        06_exception_handling.py
        07_file_io.py
        08_modules_and_builtins.py

使用方式（推荐用 uv，本项目根目录已有 .venv）：
    uv run python main.py
    uv run python main.py 03      # 直接跑编号 03 的示例
    uv run python main.py all     # 跑全部

每个示例文件都内含详细中文注释，并指明对应 Java 写法。
"""
from __future__ import annotations

import sys
import runpy
from pathlib import Path

# Windows 控制台默认 GBK，中文会乱码。
# 这里强制把 stdout/stderr 切到 UTF-8，让 print 的中文能正常显示。
# 在 macOS / Linux 上是 no-op，不影响行为。
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass  # 旧版本 Python / 已被重定向的流，跳过即可

BASICS_DIR = Path(__file__).parent / "basics"

# 编号 -> 文件名 的映射（保持有序，方便后续插入）
LESSONS: dict[str, str] = {
    "01": "01_variables_and_types.py",
    "02": "02_control_flow.py",
    "03": "03_data_structures.py",
    "04": "04_functions.py",
    "05": "05_classes.py",
    "06": "06_exception_handling.py",
    "07": "07_file_io.py",
    "08": "08_modules_and_builtins.py",
}


def print_menu() -> None:
    print("=" * 60)
    print("Python 学习菜单（对比 Java）")
    print("=" * 60)
    for code, filename in LESSONS.items():
        print(f"  {code}  {filename}")
    print("  all 依次运行所有示例")
    print("  q   退出")
    print("=" * 60)


def run_one(code: str) -> None:
    """通过 runpy 运行指定编号的示例文件"""
    filename = LESSONS.get(code)
    if not filename:
        print(f"未找到编号 {code} 对应的示例")
        return
    path = BASICS_DIR / filename
    print(f"\n>>> 运行 {code}: {filename}\n")
    # runpy.run_path 相当于 import 然后 __main__ 跑一遍
    runpy.run_path(str(path), run_name="__main__")
    print(f"\n<<< {code} 运行结束\n")


def run_all() -> None:
    for code in sorted(LESSONS.keys()):
        run_one(code)


def main() -> None:
    args = sys.argv[1:]

    if not args:
        # 交互式菜单
        print_menu()
        try:
            choice = input("请输入要运行的编号（或 all / q）：").strip()
        except EOFError:
            choice = "q"

        if choice.lower() in ("q", "quit", "exit"):
            print("Bye!")
            return
        if choice.lower() == "all":
            run_all()
            return
        run_one(choice)
        return

    # 命令行参数模式
    target = args[0]
    if target == "all":
        run_all()
    else:
        run_one(target)


if __name__ == "__main__":
    main()
