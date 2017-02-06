def minMutation(start, end, bank):
    indexes=[]
    for i in range(8):
        if start[i]!=end[i]:
            indexes.append(i)
    res=len(indexes)
    tmp=list(start)
    tn=0
    sres=1
    for i in indexes:
        tmp[i]=end[i]
        if ''.join(tmp) not in bank and tn+1<res:
             sres=0
             break
        else:
            tn+=1
    tmp=list(end)
    tn=0
    eres=1
    for i in indexes:
        tmp[i]=start[i]
        if ''.join(tmp) not in bank and tn+1<res:
            eres=0
            break
        else:
            tn+=1

    return res if sres or eres else -1


if __name__=="__main__":
    print minMutation("AACCGGTT","AACCGGTA",["AACCGGTA"])
    print minMutation("AACCGGTT","AAACGGTA",["AACCGGTA", "AACCGCTA", "AAACGGTA"])
    print minMutation("AAAAACCC","AACCCCCC",["AAAACCCC", "AAACCCCC", "AACCCCCC"])
    print minMutation("AACCGGTT",
    "AAACGGTA",
    ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"])
