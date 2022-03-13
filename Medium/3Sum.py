class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res=set()
        nums.sort()
        length=len(nums)
        if length<3:
            return []
        
        for i in range(length):
            l,r=i+1,length-1
            
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.add((nums[i],nums[l],nums[r]))
                    r-=1
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return res
