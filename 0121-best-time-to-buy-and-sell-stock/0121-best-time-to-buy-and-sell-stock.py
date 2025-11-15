class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = prices[0]
        maximum_profit = 0
        for i in range(1,len(prices)):
            if prices[i] <= min_price:
                min_price = prices[i]
                max_price = prices[i]
            elif prices[i] >= max_price:
                max_price = prices[i]
            maximum_profit = max(maximum_profit,max_price - min_price)
        return maximum_profit