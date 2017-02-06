
def longestConsecutive(nums):
    used={}
    for i in nums:
        used[i]=False
    longest=0
    for i in nums:
        if used[i]:
            continue
        length=1
        used[i]=True
        j=i+1
        while not used.get(j,True):
            used[j]=True
            j+=1
            length+=1
        k=i-1
        while not used.get(k,True):
            used[k]=True
            k-=1
            length+=1
        if length>longest:
            longest=length
    return longest
            

if __name__=="__main__":
    print longestConsecutive([100, 4, 200, 1, 3, 2])
            
