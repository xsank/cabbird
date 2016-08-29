def getSum(a, b):
    c=(a|b)<<1
    d=a^b
    return c^d
        


if __name__=="__main__":
    print getSum(1,3)
    print getSum(1,2)
    print getSum(3,3)
    print getSum(0,0)
    print getSum(4,1)
    print getSum(5,1)
    print getSum(17,11)
    print getSum(11,23)
