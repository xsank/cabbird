def combinationSum4(nums, target):
    total=[]
    genCombination(total,[],nums,target)
    print total
    return len(total)
        
        
def genCombination(total,single,nums,target):
    for i in nums:
        single.append(i)
        if sum(single)==target:
            total.append(single[:])
            single=[]
        genCombination(total,single,nums,target)
        
    
    
if __name__=="__main__":
    print combinationSum4([1,2,3],4)