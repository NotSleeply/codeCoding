#include <bits/stdc++.h>
using namespace std;

int ans;

void dfs(int num, int depth)
{
	if (num <= depth)
	{
		return;
	}
	for (int i = depth; i <= sqrt(num); i++)
	{
		if (num % i == 0)
		{
			ans++;
			dfs(num / i, i);
		}
	}
}

int main(void)
{
	int n;
	cin >> n;
	vector<int> arr(n);
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	for (int i = 0; i < arr.size(); i++)
	{
		ans = 1;
		dfs(arr[i], 2);
		cout << ans << endl;
	}
}
