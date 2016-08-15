def isIsomorphic(s, t):
    map={}
    for i,c in enumerate(s):
        if (t[i] in map.values() and c not in map) or (c in map and map[c]!=t[i]):
            return False
        else:
            map[c]=t[i]
    return True
                
    
if __name__=="__main__":
    print isIsomorphic("egg", "add")
    print isIsomorphic("foo", "bar")
    print isIsomorphic("paper", "title")
    print isIsomorphic("ab", "aa")
    print isIsomorphic("aa", "ab")
    print isIsomorphic("32767", "65535")