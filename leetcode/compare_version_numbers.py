def compareVersion(version1, version2):
    list1=version1.split(".")
    list2=version2.split(".")
    index=0
    length1=len(list1)
    length2=len(list2)
    min_length=min(length1,length2)
    while index<min_length:
        if int(list1[index])<int(list2[index]):
            return -1
        elif int(list1[index])>int(list2[index]):
            return 1
        index+=1
    if length1!=length2:
        isVersion1=True
        _list=list1
        if length1<length2:
            isVersion1=False
            _list=list2
        max_length=len(_list)
        while index<max_length:
            if int(_list[index]):
                return 1 if isVersion1 else -1
            index+=1
    return 0
 
 
if __name__=="__main__":
    print compareVersion("0.1","1.1")
    print compareVersion("1.1","1.1.1")
    print compareVersion("1.2","11.11")
    print compareVersion("1","1")
    print compareVersion("1.1","1.0")
    print compareVersion("01","1")
    print compareVersion("1.0","1")
    print compareVersion("1.0.1","1")