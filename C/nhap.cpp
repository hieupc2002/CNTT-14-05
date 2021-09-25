#include<stdio.h>
bool songto(int a)
{
	if(a==2||a==3)
		return true;
	if(a%2==0||a%3==0||a<2)
		return false;
	for(int i=5;i<=a/2;i+=6)
		if(a%i==0||a%(i+2)==0)
			return false;
	return true;
}
main()
{
	int a;
	scanf("%d",&a);
	if(songto(a))
		printf("%d la ng to",a);
	else
		printf("%d khong la ng to",a);
}
