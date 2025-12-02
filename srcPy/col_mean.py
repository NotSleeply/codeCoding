#!/usr/bin/env python3
"""计算包含两列浮点数的文件每列（从上到下）平均值，保留2位小数并打印。"""
import os
import sys


def compute_column_means(path):
    sums = []
    counts = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            # convert to floats; ignore non-numeric parts
            try:
                nums = [float(x) for x in parts]
            except ValueError:
                # skip lines that can't be parsed
                continue
            # extend sums/counts if this line has more columns
            if len(sums) < len(nums):
                for _ in range(len(nums) - len(sums)):
                    sums.append(0.0)
                    counts.append(0)
            for i, v in enumerate(nums):
                sums[i] += v
                counts[i] += 1

    means = []
    for s, c in zip(sums, counts):
        if c == 0:
            means.append(float('nan'))
        else:
            means.append(s / c)
    return means


def main():
    # 默认使用与脚本同目录下的 data.txt
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'data.txt')
    if len(sys.argv) > 1:
        data_path = sys.argv[1]

    if not os.path.exists(data_path):
        print(f"数据文件不存在: {data_path}")
        sys.exit(1)

    means = compute_column_means(data_path)
    # 打印每列均值，保留2位小数
    for i, m in enumerate(means, start=1):
        if m != m:  # NaN check
            print(f"第{i}列: NaN")
        else:
            print(f"第{i}列平均值: {m:.2f}")


if __name__ == '__main__':
    main()
