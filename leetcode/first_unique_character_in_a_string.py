def firstUniqChar(s):
    map={}
    for c in s:
        if c not in map:
            map[c]=1
        else:
            map[c]+=1
    for i,c in enumerate(s):
        if map[c]==1:
            return i
    return -1


if __name__=="__main__":
    print firstUniqChar("leetcode")
    print firstUniqChar("oo")
    print firstUniqChar("loveleetcode")
