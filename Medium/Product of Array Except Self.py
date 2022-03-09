class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        prod=1
        z_count=0
        for i in nums:
            if i==0:
                z_count+=1
                continue
            prod*=i
        if z_count>1:
            return [0]*len(nums)
        for i in nums:
            if i==0 and z_count==1:
                res.append(prod)
            elif i!=0 and z_count==1:
                res.append(0)
            else:
                res.append(int(prod/i))
        return res
