class Solution:
  #Too slow
  '''
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
  '''
  def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=n*(n+1)//2
        return s-sum(nums)
