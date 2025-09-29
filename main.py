def f(n):
    """计算并返回正整数n的所有因数之和"""
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total



if __name__ == "__main__":
    n = int(input())
    result = f(n)
    print(result)
