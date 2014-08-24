
def count_max_serial_one(num=0):
    res=tmp=0
    while num:
        tmp=tmp+1 if num&1 else 0
        res=max(res,tmp)
        num>>=1
    return res

