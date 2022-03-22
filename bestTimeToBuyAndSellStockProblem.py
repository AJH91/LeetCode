def maxProfit(prices):
    size = len(prices)
    if size < 2:
        return 0
    maxP, minP = float('-inf'), prices[0]
    #float('-inf') = Acts as an unbounded upper value for comparison
    for p in prices:
        maxP = max(maxP, p-minP)
        minP = min(minP, p)
    return maxP






print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))





