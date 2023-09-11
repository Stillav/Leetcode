# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n 
        
        while end >= 2:
            mid = (start + end) // 2
            
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            
            if isBadVersion(mid):
                end = mid -1 
                
            else:
                start = mid + 1 
            
            
        return 1 
            
            
                