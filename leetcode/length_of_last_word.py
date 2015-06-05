
def lengthOfLastWord(s):
    s=s.strip()
    if not s:
        return 0
    return len(s.split()[-1])


if __name__=="__main__":
    print lengthOfLastWord("hello world")
