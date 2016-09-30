def integerReplacement(n):
    if n==1:
        return 0
    if n&1:
        return min(integerReplacement(n+1)+1,integerReplacement(n-1)+1)
    else:
        return integerReplacement(n/2)+1


if __name__=="__main__":
    print integerReplacement(8)
    print integerReplacement(7)
