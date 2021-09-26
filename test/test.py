"""
URL:https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b
DATE:2021/09/26
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
from math import ceil,floor

def main():
    H,W = read_ints()
    if H<=1 or W<=1:
        print(1)
    else:
        ans = ceil(H/2)*ceil(W/2)+floor(H/2)*floor(W/2)
        print(ans)
    return 0

if __name__=='__main__':
    main()