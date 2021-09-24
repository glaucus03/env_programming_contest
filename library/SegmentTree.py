class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, N, f=lambda x,y : x+y, default=0):
        self.N = N
        self.size = 2**(N-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    def setTree(self,init_li):
        #配列の値をセット
        for i in range(self.N):
            self.dat[self.size+i] = init_li[i]
        #木の構築
        for i in range(self.size-1,0,-1):
            self.dat[i] = self.f(self.dat[2*i],self.dat[2*i+1])

    def update(self, i, x):
        i+=self.size
        self.dat[i] = x
        
        while i>1:
            self.dat[i>>1] = self.f(self.dat[i],self.dat[i^1])
            i>>=1

    def query(self, l, r):
        res = self.default

        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                res = self.f(res, self.dat[l])
                l += 1
            if r & 1:
                res = self.f(res, self.dat[r - 1])
            l >>= 1
            r >>= 1
        return res