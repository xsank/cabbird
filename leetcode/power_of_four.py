def isPowerOfFour(num):
    count=0
    index=0
    one=1
    while num>=one and count<=1:
        if num&one:
            count+=1
        index+=1
        one<<=1
    return bool(index&1 and count==1)



if __name__=="__main__":
    print isPowerOfFour(78)
    print isPowerOfFour(4)
    print isPowerOfFour(1)
    print isPowerOfFour(64)
