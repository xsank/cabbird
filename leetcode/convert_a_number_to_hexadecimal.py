def toHex(num):
    MAX=4294967296
    if num<0:
        num+=MAX
    dic="0123456789abcdef"
    t=28
    flag=15<<t
    res=[]
    while flag:
        h=(flag&num)>>t
        if h or res:
            res.append(dic[h])
        flag>>=4
        t-=4
    return ''.join(res) if res else '0'


if __name__=="__main__":
    print toHex(26)
    print toHex(0)
    print toHex(-1)
    print toHex(2147483647)
