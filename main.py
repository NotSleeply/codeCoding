# 读取输入的正整数n
n = int(input())

# 确保n是奇数，如果是偶数则减1
if n % 2 == 0:
    n -= 1

total = 0  # 总和
current_factorial = 1  # 当前阶乘值

# 遍历1, 3, 5, ..., n
for i in range(1, n + 1, 2):
    # 计算i的阶乘
    # 优化：利用前一个奇数的阶乘计算当前阶乘
    if i == 1:
        current_factorial = 1
    else:
        # 例如：5! = 3! × 4 × 5
        current_factorial *= (i - 1) * i

    # 累加当前阶乘到总和
    total += current_factorial

# 输出结果
print(f"n = {n}, s = {total}")
