def getPermutation(n, k):
    res,s=[],[]
    m=1
    for i in range(1,n+1):
        s.append(i)
        m*=i
    while n:
        m/=n
        i=(k-1)/m
        res.append(s.pop(i))
        n-=1
        k%=m
    res=map(str,res)
    return ''.join(res)


if __name__=="__main__":
    print getPermutation(3,4)
    print getPermutation(4,11)
