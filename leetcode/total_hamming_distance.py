def totalHammingDistance(nums):
    res=0
    for i in range(31):
        zero_count=0
        one_count=0
        for n in nums:
            if n&(1<<i):
                one_count+=1
            else:
                zero_count+=1
        res+=zero_count*one_count
    return res


if __name__=="__main__":
    print totalHammingDistance([4,14,2])
