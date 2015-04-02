
def atoi(str):
    _str=str.strip()
    if len(_str)==0:
        return 0
    sign=1
    flag=0
    if _str[0]=="+":
        sign=1
        flag=1
    if _str[0]=="-":
        sign=-1
        flag=1
    res=0
    for c in _str[flag:]:
        t=ord(c)-ord('0')
        if t>=0 and t<=9:
            res=res*10+t
        else:
            break
    res=res*sign
    INT_MAX=2147483647
    INT_MIN=-2147483648
    if res>INT_MAX:
        res=INT_MAX
    if res<INT_MIN:
        res=INT_MIN
    return res


if __name__=="__main__":
    print atoi("1")
    print atoi("+5 43 53636 ")
    print atoi("12355")
    print atoi("-434")
    print atoi("-5435gaaf")
    print atoi("   +0 123")
