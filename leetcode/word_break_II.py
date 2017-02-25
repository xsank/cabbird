
def wordBreak(s,wordDict):
    res=[]
    cache={w:1 for w in wordDict}
    dp=[True]
    length=len(s)
    for i in range(1,length+1):
        t=False
        for j in range(i):
            if cache.get(s[j:i],0) and dp[j]:
                t=True
                break
        dp.append(t)
    dfs(s,0,cache,[],res,dp)
    return res


def dfs(s,start,dict,ws,res,dp):
    if start==len(s):
        res.append(" ".join(ws))
    else:
        for i in range(start+1,len(s)+1):
            if dict.get(s[start:i],0) and dp[i]:
                tws=ws[:]
                tws.append(s[start:i])
                dfs(s,i,dict,tws,res,dp)


if __name__=="__main__":
    print wordBreak("abc",["ab","c"])
    print wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])
    print wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
