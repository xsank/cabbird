def magicalString(n):
    s=[1,2,2]
    for i in range(2,n):
        s+=s[i]*[3-s[-1]]
    return s[:n].count(1)


if __name__=="__main__":
    print magicalString(6)
