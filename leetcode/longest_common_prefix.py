
def longestCommonPrefix(strs):
    if not strs:
        return ''
    if len(strs)==1:
        return strs[0]
    length=len(strs[0])
    index=0
    flag=1
    while index<length and flag:
        for s in strs[1:]:
            if not s.startswith(strs[0][:index+1]):
                flag=0
                break
        if flag:
            index+=1
    return strs[0][:index]


if __name__=="__main__":
    print longestCommonPrefix(["adb","df","c"])
    print longestCommonPrefix(["","df","d"])
    print longestCommonPrefix(["abc","abc","abc"])
    print longestCommonPrefix(["abcddd","ab","abcedf"])
    print longestCommonPrefix(["adb"])
    print longestCommonPrefix([""])
    print longestCommonPrefix([])
