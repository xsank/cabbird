def rangeBitwiseAnd(m, n):
    magic=2147483647
    while m&magic != n&magic:
        magic<<=1
    return m&magic


if __name__=="__main__":
    print rangeBitwiseAnd(5,7)
    print rangeBitwiseAnd(7,8)
    print rangeBitwiseAnd(5,2147483647)
