def ladderLength(beginWord,endWord,wordList):

    def buildPath(trace,level,s,e,t,res):
        if s==e:
            res.append(t)
        else:
            if level<len(trace):
                item=trace[level]
                for i in item:
                    if s in i:
                        tmp=t[:]
                        tmp.append(i[s])
                        buildPath(trace,level+1,i[s],e,tmp,res)
        
    queue=[beginWord,""]
    alphas=[chr(i) for i in range(97,123)]
    cache={word:1 for word in wordList}
    trace=[[]]
    level=0
    stop=False
    res=[]
    while queue:
        s=queue.pop(0)
        if s:
            ts=list(s) 
            for i,c in enumerate(ts):
                for alpha in alphas:
                    if alpha!=c:
                        ts[i]=alpha
                        t=''.join(ts)
                        if cache.get(t,0):
                            trace[level].append({s:t})
                            if t==endWord:
                                stop=True
                            else:
                                queue.append(t)
                                cache[t]=0
                        ts[i]=c
        else:
            if stop:
                queue=[]
            if queue:
                queue.append("")
                trace.append([])
                level+=1
    buildPath(trace,0,beginWord,endWord,[beginWord],res)
    return res


if __name__=="__main__":
    print ladderLength("a","c",["a","b","c"])
    print ladderLength("red","tax",["ted","tex","red","tax","tad","den","rex","pee"])
    #right answer :[["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
    print ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])
