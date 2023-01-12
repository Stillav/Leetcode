class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return 1 
        elif n==0:
            return 0
        dp = [0] * (n+1)
    
        dp[1] = 1
        dp[0] = 0
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]