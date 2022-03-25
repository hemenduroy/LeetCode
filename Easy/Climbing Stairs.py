class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        dp=[1,2]
        
        for i in range(2,n):
            dp.append(dp[i-2]+dp[i-1])
        return dp[-1]
'''
recursive solution - time limit exceeded
class Solution:
    def climbStairs(self, n: int) -> int:
        ways=0
        def recurfunc(rem):
            nonlocal ways
            if rem==0:
                ways+=1
            if rem>0:
                recurfunc(rem-1)
            if rem>1:
                recurfunc(rem-2)
            return ways
        return recurfunc(n)
'''
