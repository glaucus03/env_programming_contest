def BaseNto10(X,n):
    res = 0
    for i in range(1,len(str(X))+1):
        res += int(X[-i])*(n**(i-1))
    return res