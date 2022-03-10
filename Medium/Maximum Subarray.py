class Solution:
    #Time Limit Exceeded
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        for j in range(len(nums)):
            if j==len(nums)-1:
                return max(maxsum,nums[j])
            cursum=nums[j]
            maxsum=max(cursum,maxsum)
            for i in range(j+1,len(nums)):
                cursum+=nums[i]
                maxsum=max(cursum,maxsum)
        return maxsum
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        curSum=0
        for n in nums:
            if curSum<0:
                curSum=0
            curSum+=n
            maxSum=max(maxSum,curSum)
        return maxSum
