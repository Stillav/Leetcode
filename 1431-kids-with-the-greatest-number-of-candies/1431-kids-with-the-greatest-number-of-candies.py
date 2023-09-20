class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can = max(candies)
        result = list()
        for candy in candies:
            result.append((candy + extraCandies) >= max_can)
            
        return result