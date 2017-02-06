def minWindow(s,t):
    target=[]
    indexes=[]
    res=""
    minlen=1<<31
    for i,c in enumerate(s):
        if c in t:
            if c not in target:
                target.append(c)
                indexes.append(i)
            else:
                index=target.index(c)
                target.remove(c)
                indexes.pop(index)
                indexes.append(i)
                target.append(c)
            if len(set(target))==len(t):
                ts=s[indexes[0]:indexes[-1]+1]
                tlen=len(ts)
                if tlen<minlen:
                    minlen=tlen
                    res=ts
    return res

if __name__=="__main__":
    print minWindow("ADOBECODEBANC","ABC")
