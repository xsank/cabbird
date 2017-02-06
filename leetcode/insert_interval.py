from structure.interval import *


def insert(intervals,newInterval):
    res=[]
    mids=[]
    merged=False
    
    def merge():
        if mids:
            res.append(Interval(min(mids[0].start,newInterval.start),max(mids[-1].end,newInterval.end)))
        else:
            res.append(newInterval)
        
    for i in intervals:
        if i.end<newInterval.start:
            res.append(i)
        elif i.start<=newInterval.start and i.end>=newInterval.start:
            mids.append(i)
        elif i.start>=newInterval.start and i.end<=newInterval.end:
            mids.append(i)
        elif i.start<=newInterval.end and i.end>=newInterval.end:
            mids.append(i)
        else:
            if not merged:
                merge()
                merged=True
            res.append(i)
    if not merged:
        merge()
    return res


if __name__=="__main__":
    intervals=listToIntervals([1,5])
    printIntervals(insert(intervals,Interval(2,3)))
    intervals=listToIntervals([1,3],[6,9])
    printIntervals(insert(intervals,Interval(2,5)))
    intervals=listToIntervals([1,2],[3,5],[6,7],[8,10],[12,16],[17,19])
    printIntervals(insert(intervals,Interval(4,9)))
