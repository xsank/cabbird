
def threeSumClosest(nums,target):
    length=len(nums)
    if length<=3:
        return sum(nums)
    nums.sort()
    min_gap=1<<31
    result=0
    for i,n in enumerate(nums[:-2]):
        left=i+1
        right=length-1
        while left<right:
            s=nums[i]+nums[left]+nums[right]
            gap=abs(target-s)
            if gap<min_gap:
                min_gap=gap
                result=s
            if s>target:
                right-=1

            elif s<target:
                left+=1
            else:
                break
    return result


if __name__=="__main__":
    print threeSumClosest([-1,2,1,-4],1)
