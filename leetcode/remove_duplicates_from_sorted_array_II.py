
def removeDuplicates(nums):
    extras=[]
    flag=1<<32
    count=0
    for i in nums:
        if i!=flag:
            flag=i
            count=1
        else:
            count<<=1
            if count>2:
                extras.append(i)
    for i in extras:
        nums.remove(i)
    return len(nums)


if __name__=="__main__":
    print removeDuplicates([1,1,1,2,2,3])
    print removeDuplicates([-1,0,1,1,1,2,2,2,3,3,3])

