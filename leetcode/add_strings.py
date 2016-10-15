def addStrings(num1, num2):
    result=[]
    len1,len2=len(num1),len(num2)
    _long,_short=(len1,len2) if len1>=len2 else (len2,len1)
    eindex=0
    flag=0
    while eindex<_long:
        index=-1-eindex
        n1=int(num1[index]) if eindex<len1 else 0
        n2=int(num2[index]) if eindex<len2 else 0
        s=n1+n2+flag
        flag,res=s/10,s%10
        result.insert(0,str(res))
        eindex+=1
    if flag:
        result.insert(0,'1')
    return ''.join(result)


if __name__=="__main__":
    print addStrings("896","432546")
    print addStrings("1","9")
