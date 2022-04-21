class Solution:
    def maxHeight(self, A):
        
        def isSmaller(a,b):
            return a[0]<=b[0] and a[1]<=b[1] and a[2]<=b[2]
        
        
        A = [[0, 0, 0]] + sorted(map(sorted, A))
        dp = [0] * len(A)
        for j in range(1, len(A)):
            for i in range(j):
                if isSmaller(A[i],A[j]):
                    dp[j] = max(dp[j], dp[i] + A[j][2])
        return max(dp)
