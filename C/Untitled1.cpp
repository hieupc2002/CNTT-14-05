#include <stdio.h>
#include <time.h>
void BubbleSort(int a[], int n) {
    int tmp;
    for (int i = 0; i < n; i++) {   
        for (int j = 0; j < n - i - 1; j++) { 
            if (a[j] > a[j + 1]) {  
                tmp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = tmp;
            }
        }
    }
}

void PrintArr(int a[], int n){
    for (int i = 0; i < n; i++)
        printf("%d   ", a[i]);
}

int main() {
  int a[] = {54,23,46,2,77,12,4,67,3,9,17,91,33,22,11};
  int n = sizeof(a)/sizeof(a[0]);
  printf("Mang chua sap xep:\n");
PrintArr(a,n);
clock_t start, end;
double duration;
start = clock();
BubbleSort(a, n);
end = clock();
duration = (double)(end - start) / CLOCKS_PER_SEC;
  printf("\n\nMang da sap xep:\n");
PrintArr(a,n);
printf("\nBubble Sort take %f seconds", duration);
  return 0;
}

