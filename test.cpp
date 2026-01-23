#include <bits/stdc++.h>
using namespace std;
int a[1000005],b[1000005],n;
int main(void)
{
	cin>>n;
	for(int i = 1;i<=n;i++) cin>>a[i];
	b[1]=1;
	b[2]=2;
	for(int i =3;i<=1000000;i++){
		b[i]=(2*b[i-1]+b[i-2])%32767;
	}
	for(int i=1;i<=n;i++){
		cout<<b[a[i]]<<endl;
	}
}

