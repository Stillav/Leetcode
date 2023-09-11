class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice, maxProfit = float("inf"), float("-inf")

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, (price - minPrice))
        
        return maxProfit
                
        
        