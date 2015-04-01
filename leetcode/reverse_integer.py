
def reverse(x):
    tmp=abs(x)
    flag=tmp==x
    res=0
    while tmp:
        res=res*10+tmp%10
        tmp/=10
    if (res & 0x7fffffff)!=res:
        return 0
    return res if flag else -res


if __name__=="__main__":
    print reverse(-2147483412)
    print reverse(10)
    print reverse(1534236469)
    print reverse(123)
    print reverse(4)
    print reverse(-123)
