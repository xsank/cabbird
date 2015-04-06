
def convertToTitle(num):
    res=[]
    while num:
        t=num%26
        if not t:
            t=26
            num-=1
        res.insert(0,chr(t+64))
        num/=26
    return ''.join(res)


if __name__=="__main__":
    print convertToTitle(1)
    print convertToTitle(26)
    print convertToTitle(28)
    print convertToTitle(52)
    print convertToTitle(27)

