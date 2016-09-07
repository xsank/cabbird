def threeSum(nums):
    total=[]
    length=len(nums)
    nums=sorted(nums)
    for i in range(length-2):
        for j in range(i+1,length-1):
            for k in range(j+1,length):
                res=[nums[i],nums[j],nums[k]]
                if sum(res)==0:
                    res=sorted(res)
                    if res not in total:
                        total.append(res)
                    break
    return total


if __name__=="__main__":
    print threeSum([1,2])
    print threeSum([1,-1,-1,0])
    print threeSum([1,0,-1])
    print threeSum([-1, 0, 1, 2, -1, -4])
    print threeSum([13,4,-6,-7,-15,-1,0,-1,0,-12,-12,9,3,-14,-2,-5,-6,7,8,2,-4,6,-5,-10,-4,-9,-14,-14,12,-13,-7,3,7,2,11,7,9,-4,13,-6,-1,-14,-12,9,9,-6,-11,10,-14,13,-2,-11,-4,8,-6,0,7,-12,1,4,12,9,14,-4,-3,11,10,-9,-8,8,0,-1,1,3,-15,-12,4,12,13,6,10,-4,10,13,12,12,-2,4,7,7,-15,-4,1,-15,8,5,3,3,11,2,-11,-12,-14,5,-1,9,0,-12,6,-1,1,1,2,-3])
