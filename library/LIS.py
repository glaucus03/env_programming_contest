import bisect

def LIS(seq):
    INF = max(seq) + 1
    res = [INF] * len(seq)
    tmp = -1
    LIS_length = 0
    
    for i in range(len(seq)):
        idx = bisect.bisect_left(res,seq[i]) 
        
        if idx>tmp:
            tmp = idx
            LIS_length+=1

        else:
            pass    
        
        res[idx] = seq[i]
      
    return LIS_length

seq = [1,3,5,2,4,6]
ans = LIS(seq)
print(ans)