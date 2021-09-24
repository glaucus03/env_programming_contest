class LazySegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, N, f=lambda x,y : x+y, default=0):
        self.N = N
        self.size = 2**(N-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f
        
        self.lazy = [None]*(self.size*2)

    def setTree(self,init_li):
        #配列の値をセット
        for i in range(self.N):
            self.dat[self.size+i] = init_li[i]
        #木の構築
        for i in range(self.size-1,0,-1):
            self.dat[i] = self.f(self.dat[2*i],self.dat[2*i+1])
    
    def gindex(self,l,r):
        """
        伝播する対象区間を求める
        """
        l+= self.size
        r+= self.size
        
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        
        while r>l:
            if l<=lm:
                yield l
            if r <=rm:
                yield r
            r>>=1
            l>>=1
        while l:
            yield l
            l>>=1
    def propagates(self,*ids):
        """
        遅延伝播
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.dat[2 * i] = v
            self.dat[2 * i + 1] = v
            self.lazy[i] = None

    def update(self, l, r, x):
        """
        区間[l, r)の値をxに更新
        l, r: index(0-index)
        x: update value
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.dat[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.dat[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.dat[i] = self.f(self.dat[2 * i], self.dat[2 * i + 1])


    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

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
        