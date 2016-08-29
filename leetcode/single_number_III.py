def singleNumber(nums):
    xor=reduce(lambda x,y:x^y,nums)
    lb=xor&-xor
    a=b=0
    for n in nums:
        if n&lb:
            a^=n
        else:
            b^=n
    return [a,b]


if __name__=="__main__":
    print singleNumber([1, 2, 1, 3, 2, 5])
