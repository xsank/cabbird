def findWords(words):
    res=[]
    rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
    for w in words:
        record=[0,0,0]
        sw=set(w.lower())
        for c in sw:
            for i,r in enumerate(rows):
                if c in r:
                    record[i]=1
        if sum(record)==1:
            res.append(w)
    return res


if __name__=="__main__":
    print findWords(["Hello", "Alaska", "Dad", "Peace"])
    print findWords(["Aasdfghjkl","Qwertyuiop","zZxcvbnm"])
