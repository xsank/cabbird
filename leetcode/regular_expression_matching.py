
def isMatch(s, p):
    index=0
    length=len(s)
    while index<length:
        


if __name__=="__main__":
    print isMatch("aa","a")
    print isMatch("aa","aa")
    print isMatch("aaa","aa")
    print isMatch("aa","a*")
    print isMatch("aa",".*")
    print isMatch("ab",".*")
    print isMatch("aab","c*a*b")
