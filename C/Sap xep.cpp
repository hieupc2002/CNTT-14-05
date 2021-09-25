#include<stdio.h>
main()
{
	int a[6]={200,186,46,15,24,127};
	int vtmin;
	for(int i=0;i<5;i++){
		for(int j=i+1;j<6;j++)
		{
			if(a[i]>a[j])
			{
				int temp=a[i];
				a[i]=a[j];
				a[j]=temp;
				for(int i=0;i<6;i++)
				{
					printf("%5d",a[i]);
				}
				printf("\n",a[i]);
			}
		}
	}
	for(int i=0;i<6;i++)
	{
		printf("%5d",a[i]);
	}
}
