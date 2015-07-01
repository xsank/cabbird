
def generate(numRows):
    res=[]
    lr=r=[]
    for i in range(numRows):
        r=[0]
        for j in range(i):
            r.append(lr[j]+lr[j+1])
        r.append(1)
        lr=r
        res.append(lr[1:])
    return res


if __name__=="__main__":
    print generate(5)
    print generate(1)
    print generate(0)
