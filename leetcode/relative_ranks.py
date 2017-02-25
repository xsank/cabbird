def findRelativeRanks(nums):
    res=[]
    snums=sorted(nums,reverse=True)
    _map={}
    name_map={
        1:"Gold Medal",
        2:"Silver Medal",
        3:"Bronze Medal"
    }

    def name(index):
        return name_map.get(index,str(index))

    for i,c in enumerate(snums):
        _map[c]=i+1
    for n in nums:
        res.append(name(_map[n]))
    return res


if __name__=="__main__":
    print findRelativeRanks([6,4,3,2,1])
