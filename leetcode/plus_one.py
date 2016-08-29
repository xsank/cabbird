def plusOne(digits):
    flag,res=1,[]
    for i in digits[::-1]:
        t=i+flag
        i,flag=(0,1) if t==10 else (t,0)
        res.insert(0,i)
    if flag:
        res.insert(0,1)
    return res


if __name__=="__main__":
    print plusOne([9,9,9,9])
    print plusOne([1,9,9,9,9])
    print plusOne([1,9,9,9,8])
    print plusOne([1])
    print plusOne([1,9,9,2,9])
