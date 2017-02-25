def palindromePairs(words):
    res=[]
    _map={}
    palindromes=[]
    empty=-1
    for i,w in enumerate(words):
        if not w:
            empty=i
        _map[w]=i
    for i,w in enumerate(words):
        rw=w[::-1]
        if rw in _map and rw!=w:
            res.append([i,_map[rw]])
        else:
            wlen=len(rw)
            for j in range(wlen-1):
                if isPalindrome(rw[:j+1]) and rw[j+1:] in _map:
                    res.append([i,_map[rw[j+1:]]])
            for j in range(wlen-1):
                if isPalindrome(rw[j+1:]) and rw[:j+1] in _map:
                    res.append([i,_map[rw[:j+1]]])
            if j==wlen-2:
                palindromes.append(i)
    if empty>=0:
        for p in palindromes:
            res.append([empty,p])
    return res
        


def isPalindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True



if __name__=="__main__":
    print palindromePairs(["bat", "tab", "cat"])
    print palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
