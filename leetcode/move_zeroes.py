def moveZeroes(nums):
    indexes=[i for i,n in enumerate(nums) if n==0]
    for i,n in enumerate(indexes):
        nums.pop(n-i)
        nums.append(0)
    return nums
            
    
if __name__=="__main__":
    print moveZeroes([0, 1, 0, 3, 12])
    print moveZeroes([0, 0])
    print moveZeroes([1, 0, 0])