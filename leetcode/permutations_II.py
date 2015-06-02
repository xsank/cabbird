
def findAllPermutations(total,remain,result):
    if not remain:
        total.append(result)
        return
    flag=[]
    for i in remain:
        if i not in flag:
            flag.append(i)
            rem=remain[:]
            rem.remove(i)
            res=result[:]
            res.append(i)
            findAllPermutations(total,rem,res)

def permuteUnique(nums):
    total=[]
    findAllPermutations(total,nums,[])
    return total

if __name__=="__main__":
    print permuteUnique([1,2,1])

