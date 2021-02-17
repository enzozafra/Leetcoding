class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)
        
        if p == '':
            return True if s == '' else False
        
        dp = [ [False for _ in range(s_len+1)] for _ in range(p_len+1)]

        dp[0][0] = True
        
        # for an empty string, only a '*' will match
        # empty string because index 0
        for p_idx in range(1, p_len+1):
            if p[p_idx-1] == '*':
                dp[p_idx][0] = dp[p_idx-1][0]
        
        for p_index in range(1, p_len+1):
            for s_index in range(1, s_len+1):
                
                if p[p_index - 1] == '*':
                    dp[p_index][s_index] = dp[p_index-1][s_index] or dp[p_index][s_index-1]
                
                elif p[p_index - 1] == '?' or p[p_index-1] == s[s_index-1]:
                    dp[p_index][s_index] = dp[p_index-1][s_index-1]
                
                else:
                    dp[p_index][s_index] = False
        
        return dp[-1][-1]
                    