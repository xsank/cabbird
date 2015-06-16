
def sortColors(nums):
    total=[0,0,0]
    for i in nums:
        total[i]+=1
    index=0
    for i,count in enumerate(total):
        while count>0:
            nums[index]=i
            index+=1
            count-=1
    return nums


if __name__=="__main__":
    print sortColors([0,0,0,1,1,1,2,2,2,0,0])
    print sortColors([])
    print sortColors([0])
