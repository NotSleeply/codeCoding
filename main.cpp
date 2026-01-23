#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    int n;
    cin >> n;
    int res = 0;
    vector<vector<char>> arr(n, vector<char>(n));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == '@')
            {
                res++;
            }
        }
    }
    int x;
    cin >> x;
    while (x--)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (arr[i][j] == '!')
                {
                    arr[i][j] = '@';
                    res++;
                }
                else if (arr[i][j] == '@')
                {
                    if (i > 0 && arr[i - 1][j] == '.')
                    {
                        arr[i - 1][j] = '!';
                    }
                    if (j > 0 && arr[i][j - 1] == '.')
                    {
                        arr[i][j - 1] = '!';
                    }
                    if (i < n - 1 && arr[i + 1][j] == '.')
                    {
                        arr[i + 1][j] = '!';
                    }
                    if (j < n - 1 && arr[i][j + 1] == '.')
                    {
                        arr[i][j + 1] = '!';
                    }
                }
            }
        }
    }
    cout << res;
}
