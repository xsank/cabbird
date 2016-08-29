def maxProfit(prices):
    length=len(prices)
    if length==0:
        return 0
    _min=prices[0]
    _max=0
    for i in range(1,length):
        t=prices[i]-_min
        if prices[i]<_min:
            _min=prices[i]
        if t>_max:
            _max=t
    return _max


if __name__=="__main__":
    print maxProfit([])
    print maxProfit([1,2])
    print maxProfit([7, 1, 5, 3, 6, 4])
    print maxProfit([7, 6, 4, 3, 1])
