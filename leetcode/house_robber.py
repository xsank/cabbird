
def rob(num):
    length=len(num)
    res=[0]*length
    if length==0:
        return 0
    if length>0:
        res[0]=num[0]
    if length>1:
        res[1]=max(num[0],num[1])
    for i in range(2,length):
        res[i]=max(res[i-2]+num[i],res[i-1])
    return res[length-1]

if __name__=="__main__":
    print rob([1])
    print rob([2,1])
    print rob([1,2,3])
    print rob([1,2,3,4,5,6,7])
