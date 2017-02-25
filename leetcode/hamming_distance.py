def hammingDistance(x, y):
    t=x^y
    res=0
    while t:
        res+=1
        t=t&(t-1)
    return res


if __name__=="__main__":
    print hammingDistance(1,4)
