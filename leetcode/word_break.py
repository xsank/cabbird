
def wordBreak(s,dict):
    length=len(s)
    indexes=range(length)
    for ts in dict:
        index=s.find(ts)
        end=index+len(ts)
        if index>=0:
            for i in range(index,end):
                indexes[i]=-1
    return -sum(indexes)==length



if __name__=="__main__":
    #print wordBreak("leetcod",["leet","code"])
    print wordBreak("abcd",["a","abc","b","cd"])
