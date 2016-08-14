def groupAnagrams(strs):
    result={}
    for s in strs:
        cdict=[0 for i in range(26)]
        for i in s:
            cdict[ord(i)-97]+=1
        klist=[]
        for i,n in enumerate(cdict):
            if n>0:
                klist.append(chr(i+97)*n)
        key=''.join(klist)
        if key in result:
            result[key].append(s)
        else:
            result[key]=[s]
    return result.values()
    

if __name__=="__main__":
    print groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print groupAnagrams(["cab","pug","pei","nay","ron","rae","ems","ida","mes"])