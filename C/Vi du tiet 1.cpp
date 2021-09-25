#include<bits/stdc++.h>
using namespace std;
int fib(int n)
{
	/*int s=0,v=1,f;
	for (int i=0 ; i<=n;i++)
	{
		s=v+s;
		v=f;
		s=v;
	}*/
	if(n<=1) return n;
	return fib(n-1)+fib(n-2);
}
int main()
{
	int n=10;
	cout << fib(n);
	getchar();
	return 0;
}
