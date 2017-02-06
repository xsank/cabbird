def restoreIpAddresses(s):
    length=len(s)
    res=[]
    if length<4 or length>12:
        return res

    def isValid(s):
        if s[0]=="0" and len(s)>1:
            return False
        return 0<=int(s)<=255

    for i in range(3):
        for j in range(i+1,length-2):
            for k in range(j+1,length-1):
                print i,j,k
                if isValid(s[:i+1]) and isValid(s[i+1:j+1]) and isValid(s[j+1:k+1]) and isValid(s[k+1:]):
                    res.append("%s.%s.%s.%s" % (s[:i+1],s[i+1:j+1],s[j+1:k+1],s[k+1:]))
    return res


if __name__=="__main__":
    print restoreIpAddresses("0000")
    print restoreIpAddresses("1111")
    print restoreIpAddresses("25525511135")
