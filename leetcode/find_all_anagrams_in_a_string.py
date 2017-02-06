from collections import Counter


def findAnagrams(s, p):
    def compare(a,b):
        return len(a-b)==0
    res=[]
    i=g=0
    flag=Counter(p)
    lens=len(s)
    lenp=len(p)
    t=Counter()
    while i<lens:
        print i
        if s[i] in flag:
            if t[s[i]]==flag[s[i]]:
                print i,t,flag
                if compare(flag,t):
                    res.append(i-lenp-g)
                t=Counter()
                g=0
            t[s[i]]+=1
        else:
            g+=1
        i+=1
    if compare(flag,t):
        res.append(i-lenp-g)
    return res
            

if __name__=="__main__":
    print findAnagrams("cbaebabacd","abc")
    print findAnagrams("abab","ab")
