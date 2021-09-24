"""
URL:https://atcoder.jp/contests/typical90/tasks/typical90_bl
DATE:2021/09/24
"""
import sys
# sys.setrecursionlimit(10**9)
# from copy import deepcopy
# from decimal import Decimal
# from math import ceil,floor
# from collections import deque,Counter
# from heapq import heapify,heappop,heappush
# from itertools import accumulate,product,permutations,combinations,combinations_with_replacement
# from bisect import bisect_left,bisect_right
# from functools import lru_cache#@lru_cache(maxsize=None)

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

read_int = lambda y = 0: int(readline()) + y
read_ints = lambda y = 0: map(lambda x: int(x) + y,readline().split())
read_str = lambda: readline().rstrip()
read_strs = lambda: readline().rstrip().split()
read_ints_list = lambda y = 0: list(map(lambda x:int(x) + y,readline().split()))
read_ints_array = lambda h, y = 0:list(list(map(lambda x:int(x)+y,readline().split())) for _ in range(h))
read_strs_list = lambda: list(map(str,list(readline().rstrip())))
read_strs_array = lambda h:list(list(readline().rstrip()) for _ in range(h))

# solve

def main():
    N,Q = read_ints()
    A = read_ints_list()
    B = [0]*(N)
    
    ans = 0
    for i in range(N-1):
        B[i] = A[i+1]-A[i]
        ans += abs(B[i])
    
    for i in range(Q):
        l,r,v = read_ints()
        l-=1
        r-=1
        
        tmp1 = abs(B[l-1])+abs(B[r])
        if l>0:
            B[l-1] += v
        if r<(N-1):
            B[r] -= v
        tmp2 = abs(B[l-1])+abs(B[r])
        ans+=(tmp2-tmp1)
        print(ans)
    
    
        
if __name__=='__main__':
    main()