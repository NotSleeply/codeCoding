#!/usr/bin/env python3
"""读取 `score.txt` 并按要求输出学生成绩。

输入文件：同目录下的 `score.txt`，每行格式为：
    姓名 平时成绩 期末成绩

输出格式：先输出表头一行，然后按文件顺序输出每个学生的记录，字段用英文逗号分隔：
    姓名,平时成绩,期末成绩,总成绩
总成绩计算：平时成绩占40%，期末成绩占60%，对结果进行四舍五入（向上取 .5）。
"""

import os
from typing import List, Tuple


def compute_total(ping: float, final: float) -> int:
    """按权重计算总成绩并四舍五入（.5 向上）。

    使用 int(x + 0.5) 来实现四舍五入，适用于非负分数。
    """
    total = ping * 0.4 + final * 0.6
    return int(total + 0.5)


def read_scores(file_path: str) -> List[Tuple[str, int, int, int]]:
    """读取给定文件，返回学生列表，每项为 (姓名, 平时, 期末, 总分)。

    忽略空行或格式不正确的行。
    """
    students = []
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 3:
                continue
            name = parts[0]
            try:
                ping = float(parts[1])
                final = float(parts[2])
            except ValueError:
                # 非数字分数，跳过
                continue
            total = compute_total(ping, final)
            students.append((name, int(ping), int(final), total))
    return students


def main() -> None:
    here = os.path.dirname(__file__)
    file_path = os.path.join(here, "score.txt")
    if not os.path.exists(file_path):
        print(f"score file not found: {file_path}")
        return
    students = read_scores(file_path)
    # 输出表头
    print("姓名,平时成绩,期末成绩,总成绩")
    for name, ping, final, total in students:
        print(f"{name},{ping},{final},{total}")


if __name__ == "__main__":
    main()
