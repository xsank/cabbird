def nextPermutation(nums):
    length=len(nums)
    if length>1:
        pos=-1
        for i in range(length-1,0,-1):
            if nums[i]>nums[i-1]:
                pos=i-1
                break
        if pos>-1:
            for i in range(length-1,0,-1):
                if nums[i]>nums[pos]:
                    nums[pos],nums[i]=nums[i],nums[pos]
                    break
        reverse(nums,pos+1,length-1)
    return nums


def reverse(nums,start,end):
    while start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1


if __name__=="__main__":
    print nextPermutation([1,2,3])
    print nextPermutation([3,2,1])
    print nextPermutation([1,1,4])
    print nextPermutation([1,3,2])
    print nextPermutation([2,3,1])
