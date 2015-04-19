
def wordBreak(s,dict):
    length=len(s)
    indexes=range(length)
    for ts in dict:
        index=s.find(ts)
        end=index+len(ts)
        if index>=0:
            for i in range(index,end):
                print i
                indexes.remove(i)
    return len(indexes)==0



if __name__=="__main__":
    #print wordBreak("leetcod",["leet","code"])
    print wordBreak("abcd",["a","abc","b","cd"])
