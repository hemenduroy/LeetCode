class Solution:
    #Using min()
    '''
    def findMin(self, nums: List[int]) -> int:
      return min(nums)
    '''
    def findMin(self, nums: List[int]) -> int:
        length=len(nums)
        for i in range(length):
            if i==length-1:
                return nums[0]
            if nums[i]<nums[i+1]:
                continue
            else:
                return nums[i+1]
