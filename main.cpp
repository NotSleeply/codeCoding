#include <bits/stdc++.h>
using namespace std;

// 判断质数
bool is_prime(long long n)
{
    if (n <= 1)
        return false;
    for (long long i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main(void)
{
    long long n;
    cin >> n;
    if (n == 1)
    {
        cout << 0 << " " << 0 << endl;
        return 0;
    }
    if (is_prime(n))
    {
        cout << n << " " << 1 << endl;
        return 0;
    }
    // 幂次分解
    for (long long i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            long long count = 0;
            while (n % i == 0)
            {
                n /= i;
                count++;
            }
            cout << i << " " << count << endl;
            return 0;
        }
    }
}
