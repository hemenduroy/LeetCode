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
  '''
  def search(self, nums: List[int], target: int) -> int:
        length=len(nums)-1
        if length==0:
            if target==nums[0]:
                return 0
            else:
                return -1
            
        l,r=length//2,length//2

        while l>=0 or r<=length:
            if l>=0 and nums[l]==target:
                return l
            elif r<=length and nums[r]==target:
                return r
            l-=1
            r+=1
        return -1
   '''
   #Binary Search
       def search(self, nums: List[int], target: int) -> int:
        length=len(nums)

        mid=length//2
        #length is 1
        if length==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        #mid is target
        if nums[mid]==target:
            return mid
        #finding if we're to the left or right of the inflection point
        #array is not pivoted
        if nums[length-1]>nums[0]:
            start=0
            end=length-1
        else:
            if nums[mid]>=nums[0]:
                if target>=nums[0]:
                    start=0
                    end=mid-1
                else:
                    start=mid+1
                    end=length-1
            else:
                if target<nums[length-1] and target<nums[mid]:
                    start=0
                    end=mid-1
                else:
                    start=mid+1
                    end=length-1

        print(start,end)
        #binary search starts
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            if target>nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return -1
