def convertToBase7(num):
    if num:
        res,bit=0,1
        flag=num>=0
        num=abs(num)
        while num:
            res+=(num%7)*bit
            bit*=10
            num/=7
        return str(res) if flag else str(-res)
    return '0'


if __name__=="__main__":
    print convertToBase7(-7)
    print convertToBase7(0)
    print convertToBase7(100)
