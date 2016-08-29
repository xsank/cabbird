def countBits(num):
    res=[0]
    for i in range(1,num+1):
        res.append(res[i&(i-1)]+1)
    return res


if __name__=="__main__":
    print countBits(0)
    print countBits(5)
    print countBits(9)
