def reverseVowels(s):
    slist=list(s)
    left=0
    right=len(slist)-1
    while left<right:
        if isVowel(slist[left]) and isVowel(slist[right]):
            slist[left],slist[right]=slist[right],slist[left]
        elif isVowel(slist[left]):
            left-=1
        elif isVowel(slist[right]):
            right+=1
        left+=1
        right-=1
    return ''.join(slist)
    

def isVowel(c):
    return c in "AEIOUaeiou"
    
    
if __name__=="__main__":
    print reverseVowels("hello")
    print reverseVowels("leetcode")