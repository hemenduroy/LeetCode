class Solution:
    
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: 
            tmp = last
            last = now 
            now = max(tmp + i, now)
                
        return now
