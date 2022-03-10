class Solution:
  #Using index()
  '''
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
  '''
  #Expand from center
  class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)-1
        if length==0:
            if target==nums[0]:
                return 0
            else:
                return -1
            
        mid=length//2
        l,r=mid,mid

            
        while l>=0 or r<=length:
            if l>=0 and nums[l]==target:
                return l
            elif r<=length and nums[r]==target:
                return r
            l-=1
            r+=1
        return -1
