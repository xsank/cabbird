import collections


def removeDuplicateLetters(s):
    res=[]
    counter=collections.Counter(s)
    for c in s:
        counter[c]-=1
        if c in res:
            continue
        while res and res[-1]>c and counter[res[-1]]:
            res.pop()
        res.append(c)
    return "".join(res)


if __name__=="__main__":
    print removeDuplicateLetters("bcabc")
    print removeDuplicateLetters("a")
    print removeDuplicateLetters("")
    print removeDuplicateLetters("abacb")
    print removeDuplicateLetters("cbacdcbc")
    print removeDuplicateLetters("cbadccbc")
    print removeDuplicateLetters("bbbbcaddbf")
