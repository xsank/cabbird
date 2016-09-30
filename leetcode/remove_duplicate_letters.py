def removeDuplicateLetters(s):
    return ''.join(sorted(list(set(s))))


if __name__=="__main__":
    print removeDuplicateLetters("bcabc")
    print removeDuplicateLetters("cbacdcbc")
