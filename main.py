if __name__ == "__main__":
    a = {}
    for _ in range(2):
        x = input().strip()
        b = eval(x)
        for i, j in b.items():
            if i not in a:
                a[i] = j
            else:
                a[i] += j
    # 将键分为数字和字符串两类
    c = [k for k in a.keys() if isinstance(k, int)]
    d = [k for k in a.keys() if isinstance(k, str)]
    # 分别排序
    c.sort()
    d.sort()
    # 合并排序后的键
    e = c + d
    # 构建有序字典
    f = {}
    for key in e:
        f[key] = a[key]
    # 输出结果
    print(f)
