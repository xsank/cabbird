import collections


def topKFrequent(nums, k):
    clist=collections.Counter(nums).most_common()
    return [clist[i][0] for i in range(k)]


if __name__=="__main__":
    print topKFrequent([1,1,1,2,2,3],2)
