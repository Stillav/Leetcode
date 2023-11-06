class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * 40
        dp[0], dp[1], dp[2] = 0, 1, 1
        
        for i in range(3, len(dp) - 2):
            dp[i] = dp[i - 3] + dp[i -2] + dp[i - 1]
        print(dp)
        return dp[n]