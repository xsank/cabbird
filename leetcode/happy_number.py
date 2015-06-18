
def isHappy(n):
    check=[]
    while 1:
        _list=[]
        while n:
            _list.append(n%10)
            n/=10
        for i in _list:
            n+=pow(i,2)
        if n==1:
            return True
        if n in check:
            return False
        check.append(n)


if __name__=="__main__":
    print isHappy(19)
    print isHappy(1)
    print isHappy(11)
