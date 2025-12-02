#!/usr/bin/env python3
"""统计文本中每个单词出现次数（不区分大小写），并按字典序写入 dic.txt。
输出格式：每行一个单词和次数，用空格分隔。
"""
import os
import sys
import re
from collections import Counter


def count_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    # 仅匹配字母序列作为单词
    words = re.findall(r"[A-Za-z]+", text)
    words = [w.lower() for w in words]
    return Counter(words)


def write_dict(counter, out_path):
    with open(out_path, 'w', encoding='utf-8') as f:
        for word in sorted(counter.keys()):
            f.write(f"{word} {counter[word]}\n")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    in_path = os.path.join(script_dir, 'freedom.txt')
    out_path = os.path.join(script_dir, 'dic.txt')
    if len(sys.argv) > 1:
        in_path = sys.argv[1]
    if len(sys.argv) > 2:
        out_path = sys.argv[2]

    if not os.path.exists(in_path):
        print(f"输入文件不存在: {in_path}")
        sys.exit(1)

    counter = count_words(in_path)
    write_dict(counter, out_path)
    print(f"已写入: {out_path}")


if __name__ == '__main__':
    main()
