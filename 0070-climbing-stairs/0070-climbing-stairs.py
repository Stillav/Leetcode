class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0]  * (n+1)
        if n==1:
            return 1
        elif n==2:
            return 2
        result[1] = 1
        result[2] = 2 
        
        for i in range(3, n+1):
            result[i] = result[i-1] + result[i-2]
            
        return result[n]