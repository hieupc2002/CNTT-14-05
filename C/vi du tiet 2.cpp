#include<bits/stdc++.h>
using namespace std;

int Sum(int n)
{
//if (n <= 1) return n;
//return fib(n-1) + fib(n-2);

/*
if (n < 1) return 0;
return Sum(n-1) + n;
*/

int S=0;
for(int i=0;i<=n;i++) {S+=i;}
return S;

}

int main ()
{
int n = 9;
cout << Sum(n);
return 0;
}
