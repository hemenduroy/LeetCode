class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        n=bin(n)[2::]
        for i in str(n):
            if i=='1':
                count+=1
        return count
