def is_rotation(str1, str2):
    return len(str1) == len(str2) and (str2 + str2).find(str1) > -1

