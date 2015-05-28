
def firstMissingPositive(nums):
    flag=0
    index=1
    for i in nums:
        if i>0:
            flag|=(1<<(i-1))
    while (flag & 1):
        flag>>=1
        index+=1
    return index


if __name__=="__main__":
    print firstMissingPositive([3,4,-1,1])
    print firstMissingPositive([1,2,0])

