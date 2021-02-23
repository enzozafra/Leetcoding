class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # if n = 3
        # _ _ _
        #          
        if n == 1:
            return 1
        
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[-1]