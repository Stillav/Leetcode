class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice, maxBenefit = float('inf'), 0
        
        for i in prices:
            minPrice = min(minPrice, i)
            maxBenefit = max(maxBenefit, i - minPrice)
            
        return maxBenefit
        