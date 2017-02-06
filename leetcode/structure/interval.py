
class Interval:
    def __init__(self,s=0,e=0):
        self.start=s
        self.end=e

    def __str__(self):
        return "%d,%d" % (self.start,self.end)


def listToIntervals(*l):
    intervals=[]
    for i in l:
        intervals.append(Interval(i[0],i[1]))
    return intervals
    


def printIntervals(intervals):
    for i in intervals:
        print i

