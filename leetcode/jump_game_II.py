def jump(nums):
    pos=last=cur=0
    length=len(nums)
    for i in range(length):
        if i>last:
            last=cur
            pos+=1
        cur=max(cur,i+nums[i])
    return pos


if __name__=="__main__":
    print jump([2,3,1,1,4])
