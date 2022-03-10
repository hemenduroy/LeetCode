class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cur_min = 1
        cur_max = 1
        res = float('-inf')
        
        for n in nums:
            tmp_max = cur_max * n
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(tmp_max, cur_min * n, n)
            
            res = max(res, cur_max)
        
        return res
