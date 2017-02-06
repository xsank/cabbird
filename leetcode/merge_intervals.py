from structure.interval import *


def merge(intervals):

    def cmp(a,b):
        return a.start-b.start
        
    res=[]
    if not intervals:
        return res
    intervals=sorted(intervals,cmp)
    length=len(intervals)
    minterval=intervals[0]
    for i in range(1,length):
        if intervals[i].start<=minterval.end:
            minterval.start=min(minterval.start,intervals[i].start)
            minterval.end=max(minterval.end,intervals[i].end)
        else:
            res.append(minterval)
            minterval=intervals[i]
    res.append(minterval)
    return res


if __name__=="__main__":
    intervals=listToIntervals([1,3],[2,6],[8,10],[15,18])
    printIntervals(merge(intervals))
    intervals=listToIntervals([1,3])
    printIntervals(merge(intervals))
    intervals=listToIntervals([1,4],[0,0])
    printIntervals(merge(intervals))
    intervals=listToIntervals([1,4],[1,1])
    printIntervals(merge(intervals))
    intervals=listToIntervals([1,3],[2,6],[8,10],[9,18])
    printIntervals(merge(intervals))
