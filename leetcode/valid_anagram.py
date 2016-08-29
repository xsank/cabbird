def isAnagram(s, t):
    return sorted(s)==sorted(t)


if __name__=="__main__":
    print isAnagram("anagram", "nagaram")
    print isAnagram("rat", "car")
