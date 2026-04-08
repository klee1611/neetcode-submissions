class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1 if s[0] != "0" else 0

        dp = [1] * n

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif i < n-1:
                dp[i] = dp[i+1]
        
            if i < n-1 and 9 < int(s[i:i+2]) < 27:
                if i < n-2:
                    dp[i] += dp[i+2]
                else:
                    dp[i] += 1
            
        return dp[0]