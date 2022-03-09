class Solution:

    #Time Limit Exceeded
    #Brute Force
    '''
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>profit:
                    profit=prices[j]-prices[i]
        return profit
    '''

    #Time Limit Exceeded
    #Brute Force - inner loop optimized
    '''
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=min(prices)
        sell=max(prices)
        if prices.index(buy)< prices.index(sell):
            profit=sell-buy
            return profit
        
        for i in range(1,len(prices)):
            for j in range(i):
                if prices[i]-min(prices[0:i])>profit:
                    profit=prices[i]-min(prices[0:i])
        return profit
    '''

    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10001
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
