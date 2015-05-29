
def canJump(nums):
    index=0
    length=len(nums)-1
    while index<length:
        if nums[index]==0:
            break
        index+=nums[index]
    return index==length


if __name__=="__main__":
    print canJump([2,3,1,1,4])
    print canJump([3,2,1,0,4])
    print canJump([3])
    print canJump([0])
    print canJump([2,0])
