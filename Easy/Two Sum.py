class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        #print(len(nums))
        for i in range (0,len(nums)):
            #print(i)
            for j in range(i+1,len(nums)):
                    sum=nums[i]+nums[j]
                    if sum == target:
                        res.append(i)
                        res.append(j)
                        return res