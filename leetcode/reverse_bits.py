
def reverseBits(n):
    bits=31
    count=0
    loop=16
    res=0
    while count<loop:
        a=(1<<count&n)<<(bits-(count<<1))
        b=(1<<(bits-count)&n)>>(bits-(count<<1))
        res|=(a|b)
        count+=1
    return res


if __name__=="__main__":
    print bin(43261596),bin(reverseBits(43261596)),reverseBits(43261596)
