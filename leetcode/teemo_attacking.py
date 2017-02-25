def findPoisonedDuration(timeSeries, duration):
    res=0
    if timeSeries:
        length=len(timeSeries)
        for i in range(1,length):
            diff=timeSeries[i]-timeSeries[i-1]
            res+=min(duration,diff)
        res+=duration
    return res


if __name__=="__main__":
    print findPoisonedDuration([], 2)
    print findPoisonedDuration([1,4], 2)
    print findPoisonedDuration([1], 2)
    print findPoisonedDuration([1,2], 2)
