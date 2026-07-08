"""
07 - 文件 I/O（对比 Java NIO / I/O 流）

== Python 与 Java 在文件 I/O 上的关键差异 ==
1. 内置 open() 一行搞定读写，比 Java 的 InputStream/OutputStream 简洁得多。
2. 强烈推荐用 with 语句（自动关闭文件，等价于 try-with-resources）。
3. 文本模式默认使用 UTF-8 编码（取决于平台）。
4. 用 pathlib.Path 操作路径，比 os.path 更面向对象（≈ Java 的 java.nio.file.Path）。
5. JSON 用标准库 json 处理（≈ Jackson / Gson）。
6. 读写 CSV 用标准库 csv（≈ Apache Commons CSV）。
"""

import json
import csv
from pathlib import Path


# ============================================================
# 1. 读取和写入文本文件
# ============================================================
# Java 写法（伪代码）：
#   try (BufferedReader br = new BufferedReader(new FileReader("demo.txt", StandardCharsets.UTF_8))) {
#       String line;
#       while ((line = br.readLine()) != null) { ... }
#   }
#
# Python 写法：
print("=== 文本文件读写 ===")
sample_path = Path("demo.txt")
sample_path.write_text("第一行\n第二行\n第三行\n", encoding="utf-8")

# 整个文件读进来
content = sample_path.read_text(encoding="utf-8")
print("read_text:")
print(content, end="")

# 逐行读取
print("readlines:")
with sample_path.open("r", encoding="utf-8") as f:   # 显式 open
    for line in f:                                    # 直接遍历 file 对象即可按行迭代
        print("  ", line.rstrip())

# 写入（覆盖）
sample_path.write_text("覆盖内容\n", encoding="utf-8")
print("覆盖后:", sample_path.read_text(encoding="utf-8"))


# ============================================================
# 2. 路径处理（pathlib）—— ≈ java.nio.file.Path
# ============================================================
print("\n=== pathlib 路径处理 ===")
p = Path(".") / "subdir" / "data.json"   # 用 / 拼接路径
print("path =", p)
print("parent =", p.parent)
print("name =", p.name)
print("suffix =", p.suffix)
print("exists? =", p.exists())

# 常用方法
sample_path.unlink(missing_ok=True)      # 删除文件，missing_ok=True 不会因为文件不存在而报错
print("删除 demo.txt 后存在?", sample_path.exists())


# ============================================================
# 3. JSON 读写
# ============================================================
print("\n=== JSON ===")
# Java 用 Jackson/Gson：
#   ObjectMapper mapper = new ObjectMapper();
#   User u = mapper.readValue(json, User.class);
#   String s = mapper.writeValueAsString(u);
#
# Python 用标准库：
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Java", "Go"],
    "active": True,
    "address": {"city": "Beijing", "zip": "100000"},
}

json_path = Path("user.json")
# 写入
json_text = json.dumps(data, ensure_ascii=False, indent=2)  # ensure_ascii=False 保留中文
json_path.write_text(json_text, encoding="utf-8")
print("写入 JSON：")
print(json_text)

# 读取
loaded = json.loads(json_path.read_text(encoding="utf-8"))
print("读回 loaded['name'] =", loaded["name"])

# 删除示例文件
json_path.unlink(missing_ok=True)


# ============================================================
# 4. CSV 读写
# ============================================================
print("\n=== CSV ===")
csv_path = Path("users.csv")
rows = [
    ["name", "age", "city"],
    ["Alice", 30, "Beijing"],
    ["Bob", 25, "Shanghai"],
]
# 写入
with csv_path.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# 读取（按字典方式）
with csv_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("  ", row)

csv_path.unlink(missing_ok=True)


# ============================================================
# 小结
# ============================================================
# - with open(...) as f: 是最常见的写法
# - pathlib 比字符串路径强大得多
# - json / csv 都是标准库，无需额外安装
