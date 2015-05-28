
def countString(s):
    last_flag=-1
    flag=-1
    res=[]
    count=1
    length=len(s)
    for i in range(length):
        if s[i]!=flag:
            last_flag=flag
            flag=s[i]
            if last_flag!=-1:
                res.append(str(count))
                res.append(last_flag)
            count=1
        else:
            count+=1
    res.append(str(count))
    res.append(flag)
    return ''.join(res)


def countAndSay(n):
    if n<1:
        return ""
    else:
        n-=1
    res="1"
    while n:
        n-=1
        res=countString(res)
    return res


if __name__=="__main__":
    print countAndSay(1)
