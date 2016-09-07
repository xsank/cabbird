def wordPattern(pattern, str):
    strs=str.split()
    return map(pattern.find,pattern)==map(strs.index,strs)


if __name__=="__main__":
    print wordPattern("abba", "dog cat cat dog")
    print wordPattern("abba", "dog cat cat fish")
    print wordPattern("aaaa", "dog cat cat dog")
    print wordPattern("abba", "dog dog dog dog")
    print wordPattern("jquery", "jquery")
