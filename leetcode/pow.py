
def myPow(x, n):
    if n<0:
        return 1.0/myPow(x,-n)
    if n==0:
        return 1
    if n==1:
        return x
    half=n>>2
    tmp=myPow(x,half)
    if n&1:
        return x*tmp*tmp
    else:
        return tmp*tmp


if __name__=="__main__":
    print myPow(2,3)
    print myPow(2,2)
    print myPow(2,1)
    print myPow(2,0)
    print myPow(2,-1)
