def findContentChildren(g, s):
    res=i=j=0
    g.sort(),s.sort()
    while j<len(s) and i<len(g):
        if s[j]>=g[i]:
            i+=1
            res+=1
        j+=1
    return res


if __name__=="__main__":
    print findContentChildren([1,2,3],[1,1])
    print findContentChildren([1,2],[1,2,3])
    print findContentChildren([10,9,8,7],[5,6,7,8])
