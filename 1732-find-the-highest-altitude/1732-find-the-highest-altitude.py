class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur, max_height = 0, 0
        
        for num in gain:
            cur += num
            if cur >= max_height:
                max_height = cur
                
        return max_height