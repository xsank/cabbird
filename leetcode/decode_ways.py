

def numDecodings(s):
    length=len(s)
    if not length:
        return 0
    res=[0]*(length+1)
    res[0]=1
    res[1]=0 if s[0]=='0' else 1
    for i in range(1,length):
        t=int(s[i-1]+s[i])
        if 9<t<27:
            res[i+1]+=res[i-1]
        t=int(s[i])
        if 0<t<10:
            res[i+1]+=res[i]
    return res[length]


if __name__=="__main__":
    print numDecodings('12')
    print numDecodings('0')
    print numDecodings('1')
    print numDecodings('120')
    print numDecodings('102')
    print numDecodings('123')
    print numDecodings('000')
    print numDecodings('1200')



