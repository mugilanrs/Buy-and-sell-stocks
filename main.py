def maxProfit(prices):
    l,r=0,1
    maxP=0
    while r< len(prices):
        if prices[l] < prices[r]:
            profit=prices[r]- prices[l]
            maxP=max(profit,maxP)
        else:
            l=r
        r=r+1
    return maxP    
        
prices=list(map(int,input().split()))
print(maxProfit(prices))
