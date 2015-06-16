
def mySqrt(x):
    if x==0:
        return 0
    last=0.0
    res=1.0
    while res!=last:
        last=res
        res=(res+x/res)/2
    return int(res)


if __name__=="__main__":
    print mySqrt(0)
    print mySqrt(1)
    print mySqrt(7)
    print mySqrt(9)
