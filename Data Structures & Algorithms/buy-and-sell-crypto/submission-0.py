class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        coinPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price > coinPrice:
                profit = (price - coinPrice)
                maxProfit = max( maxProfit, profit)
            else:
                coinPrice = price
        
        return maxProfit