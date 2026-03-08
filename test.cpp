#include <bits/stdc++.h>
using namespace std;

int main(void)
{
	int x,y;
	cin>>x>>y;
	int arr[21][21];
	arr[1][1]=1;
	for(int i =2;i<=x;i++) arr[i][1]=arr[i-1][1];
	for(int i =2;i<=y;i++) arr[1][i]=arr[1][i-1];
	for(int i =2;i<=x;i++){
		for(int j =2;j<=y;j++){
			arr[i][j]=arr[i-1][j]+arr[i][j-1];
		}
	}
	cout<<arr[x][y];
}

