class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        minBuy = prices[0]
        for price in prices:
            if price > minBuy:
                profit = max(profit, price - minBuy)
            else:
                minBuy = price
        
        return profit