
def findAllPermutations(total,remain,res):
    if not remain:
        total.append(res)
    for i in remain:
        rem=remain[:]
        rem.remove(i)
        rec=res[:]
        rec.append(i)
        findAllPermutations(total,rem,rec)

def permute(nums):
    total=[]
    findAllPermutations(total,nums,[])
    return total


if __name__=="__main__":
    print permute([1,2,3])
