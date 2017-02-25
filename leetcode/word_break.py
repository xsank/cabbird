
def _wordBreak(s,wordDict):
    return dfs(s,wordDict)


def dfs(s,dict):
    if s=="":
        return True
    else:
        dict=[w for w in dict if w in s]
        for i,w in enumerate(dict):
            index=s.find(w)
            if index==0 or index==len(s)-len(w):
                ts=s[:index]+s[index+len(w):] 
                if dfs(ts,dict):
                    return True
        return False


def wordBreak(s,wordDict):
    dp=[True]
    length=len(s)
    cache={w:1 for w in wordDict}
    for i in range(1,length+1):
        tr=False
        for j in range(i):
            if cache.get(s[j:i],0) and dp[j]:
                tr=True
                break
        dp.append(tr)
    print dp
    return dp[-1]


if __name__=="__main__":
    print wordBreak("ccbb",["bc","cb"])
    print wordBreak("cars",["car","ca","rs"])
    print wordBreak("bb",["a","b","bbb","bbbb"])
    print wordBreak("aaaaaaa",["aaaa","aaa"])
    print wordBreak("leetcode",["leet","code"])
    print wordBreak("leetcod",["leet","code"])
    print wordBreak("abcd",["a","abc","b","cd"])
    print wordBreak("abcd",["abc","cd","b"])
    print wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
