
def multiply(num1, num2):
    if num1=="0" or num2=="0":
        return "0"
    res=[]
    for i in num1:
        _sum=0
        for j in num2:
            _sum=_sum*10+int(i)*int(j)
        res.append(_sum)
    total=0
    for i in res:
        total=total*10+i
    return str(total)


if __name__=="__main__":
    print multiply("99","11")
    print multiply("12345","1")
    print multiply("12345","54321")
