def getSum(a, b):
    MAX_INT=1<<31
    MASK=1<<32
    while b:
        c=a^b
        c=c&MASK^abs(c)
        b=(a&b)<<1
        b=b&MASK^abs(b)
        a=c
    return a


if __name__=="__main__":
    print getSum(-1,1)
    print getSum(1,3)
    print getSum(1,2)
    print getSum(3,3)
    print getSum(0,0)
    print getSum(4,1)
    print getSum(5,1)
    print getSum(17,11)
    print getSum(11,23)
