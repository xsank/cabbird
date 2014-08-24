
def count_max_serial_one(num=0):
    n=num
    res=tmp=0
    while n:
        tmp=tmp+1 if n&1 else 0
        res=max(res,tmp)
        n>>=1
    return res

