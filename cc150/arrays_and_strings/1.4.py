from collections import Counter


def is_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)

