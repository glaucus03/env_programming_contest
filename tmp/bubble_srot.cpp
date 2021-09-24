#include<iostream>
using namespace std;

void trace(int N, int A[]){
    for (int i=0;i<N;i++){
        if (i>0) printf(" ");
        printf("%d",A[i]);
    }
    printf("\n");
}
int bubbleSort(int N, int A[]){
    int ans = 0;
    int idx = 0;
    bool flag = true;
    while (flag){
        flag = false;
        for (int i=N-1;i>idx;i--){
            if (A[i]<A[i-1]){
                swap(A[i],A[i-1]);
                flag = true;
                ans+=1;
            }
        }
        idx++;
    }
    return ans;
}
int main(){
    int N,ans;
    int A[100];

    scanf("%d",&N);
    for (int i=0;i<N;i++){
        scanf("%d",&A[i]);
    }

    ans = bubbleSort(N,A);
    trace(N,A);
    printf("%d",ans);
    printf("\n");

    return 0;
}