class Solution:
    #Time Limit Exceeded
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        length=len(nums)
        while length>0:
            val=nums[0]
            nums.remove(nums[0])
            length-=1
            if val in nums:
                return True
        return False
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
