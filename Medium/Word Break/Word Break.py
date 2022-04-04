class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length=len(s)
        
        dp=[False] * (length+1)
        dp[length] = True
        
        for i in range(length-1,-1,-1):
            for w in wordDict:
                if s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                    if dp[i]:
                        break
        return dp[0]
