#include<stdio.h>
#include<time.h>
int a[]= {54,34,64,1,3,9,16,2,32,19,40,7};
/*int finf(int x,int n, int m){
	if x>a[(n-1)/2] {
	find(int x)
	}
}*/
void BubbleSort(int n){
	if(n>0){
		BubbleSort(n-1);
		if(a[n]<a[n-1]){
			int temp = a[n-1];
			a[n-1]=a[n];
			a[n]=temp;
			BubbleSort(n-1);
		}
	}
	else return;
}
