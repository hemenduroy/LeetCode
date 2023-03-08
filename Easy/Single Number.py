class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            if nums[i] not in temp:
                return nums[i]
