#include<stdio.h>

void trace(int N,int A[]){
    for (int i=0;i<N;i++){
        if (i>0){
            printf(" ");
        }
        printf("%d",A[i]);
    }
    printf("\n");
}
void insertionSort(int N, int A[]){
    trace(N,A);

    for (int i=1;i<N;i++){
        int tmp = A[i];
        int j = i-1;
        while (j>=0 && A[j]>tmp){
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = tmp;
        trace(N,A);
    }
    
}

int main(){
    int N;
    int A[100];

    scanf("%d",&N);
    for (int i=0;i<N;i++){
        scanf("%d",&A[i]);
    }
    insertionSort(N,A);

    return 0;
}