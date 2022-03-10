class Solution:
    #Using min()
    '''
    def findMin(self, nums: List[int]) -> int:
      return min(nums)
    '''
    #Linear Search
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
     '''
     #Binary Search
     def findMin(self, nums: List[int]) -> int:
        length=len(nums)
        if length==1:
            return nums[0]
        if nums[length-1]>nums[0]:
            return nums[0]
        start=0
        end=length-1
        while True:
            mid=(end+start)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[start]:
                start=mid+1
            else:
                end=mid-1
