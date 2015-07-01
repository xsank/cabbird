
def getRow(rowIndex):
    lr=r=[]
    row=rowIndex+1
    for i in range(row):
        r=[0]
        for j in range(i):
            r.append(lr[j]+lr[j+1])
        r.append(1)
        lr=r
    return r[1:]


if __name__=="__main__":
    print getRow(5)
    print getRow(1)
    print getRow(0)
    print getRow(3)
