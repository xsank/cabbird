import collections


def frequencySort(s):
    counter=collections.Counter(s)
    res=[]
    for c,n in counter.most_common():
        res+=[c for i in range(n)]
    return "".join(res)


if __name__=="__main__":
    print frequencySort("tree")
    print frequencySort("cccaaa")
    print frequencySort("Aabb")
