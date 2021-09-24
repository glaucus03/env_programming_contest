/*
URL:https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_A
DATE:2021/05/02
*/

#include<iostream>
#include<algorithm>
using namespace std;

void insertion_sort(int A[],int N){
   for (int i=1;i<N;i++){
      int v = A[i];
      int j = i -1;
      while (j>=0&&A[j]>v){
         A[j+1] = A[j];
         j--;
      }
      A[j+1] = v;
   
   for (int i=0;i<N;i++){
      if (i>0) printf(" ");
      printf("%d",A[i]);
   }
   printf("\n");
   }
}
   
   
int main(){
   int N;
   int A[100];

   scanf("%d",&N);

   for (int i=0;i<N;i++) scanf("%d",&A[i]);

   for (int i=0;i<N;i++){
      if (i>0) printf(" ");
      printf("%d",A[i]);
   }
   printf("\n");
 
   insertion_sort(A,N);
   
   return 0;
}