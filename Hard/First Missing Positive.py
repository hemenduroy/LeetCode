class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length=len(nums)
        #least=min(nums)
        nums.sort()
        i=bisect.bisect_left(nums,1)
        #print(i)
        if i>=length:
            return 1
        if nums[i]>=2:
            return 1
        else:
            for j in range(i,length-1):
                if nums[j+1]-nums[j] >=2:
                    return nums[j]+1
            
        return nums[length-1]+1
