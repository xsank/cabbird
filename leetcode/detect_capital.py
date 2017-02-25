def detectCapitalUse(word):
    def isBigC(c):
        return 'A'<=c<='Z'

    total=index=0
    for i,c in enumerate(word):
        if isBigC(c):
            total+=1
            index=i
    return True if total==len(word) or (total==1 and index==0) or total==0 else False


if __name__=="__main__":
    print detectCapitalUse("USA")
    print detectCapitalUse("FlaG")
    
