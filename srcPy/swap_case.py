#!/usr/bin/env python3
"""读取 example.txt，将大写字母变小写、小写变大写，其他字符不变，结果写入 result.txt。

文件位置：与本脚本同目录下的 `example.txt` 和 `result.txt`。
实现细节：使用字符串方法 `swapcase()` 完成大小写互换，保留原文件行顺序和非字母字符。
"""

import os


def swap_file_case(src: str, dst: str) -> None:
    with open(src, 'r', encoding='utf-8') as f_in:
        content = f_in.read()
    swapped = content.swapcase()
    with open(dst, 'w', encoding='utf-8') as f_out:
        f_out.write(swapped)


def main() -> None:
    here = os.path.dirname(__file__)
    src = os.path.join(here, 'example.txt')
    dst = os.path.join(here, 'result.txt')
    if not os.path.exists(src):
        print(f'源文件不存在: {src}')
        return
    swap_file_case(src, dst)


if __name__ == '__main__':
    main()
