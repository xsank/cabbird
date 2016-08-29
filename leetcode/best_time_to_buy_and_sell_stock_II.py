def maxProfit(prices):
    end=len(prices)-1
    _sum=0
    buy=0
    flag=False
    for i in range(end):
        if prices[i+1]>prices[i] and not flag:
            buy=prices[i]
            flag=True
        if prices[i+1]<prices[i] and flag:
            _sum+=prices[i]-buy
            flag=False
    if flag:
        _sum+=prices[end]-buy
    return _sum


if __name__=="__main__":
    print maxProfit([])
    print maxProfit([1,2])
    print maxProfit([7, 1, 5, 3, 6, 4])
    print maxProfit([7, 6, 4, 3, 1])
    print maxProfit([7,3,1,8,9,1,5,10])
