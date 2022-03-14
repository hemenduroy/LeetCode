class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0,1,1,2]
        
        factor=1
        count=0
        for i in range(4,n+1):
            window=4*factor
            dp.append(1+dp[i-window])
            count+=1
            if count==window:
                count=0
                factor*=2
        
        return dp[0:n+1]
