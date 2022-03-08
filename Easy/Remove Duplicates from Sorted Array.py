class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #print(nums)
        #print(len(nums))
        '''
        for i in range(1,len(nums)):
            print(i)
            if i>=len(nums):
                break
            #print("check if "+str(nums[i])+" == "+str(nums[i-1]))
            if nums[i]==nums[i-1]:
                #print("remove "+str(nums[i]))
                nums.remove(nums[i])
                i-=1
        return len(nums)
        '''
        i=0
        while True:
            i+=1
            if i>=len(nums):
                break
            #print("check if "+str(nums[i])+" == "+str(nums[i-1]))
            if nums[i]==nums[i-1]:
                #print("remove "+str(nums[i]))
                nums.remove(nums[i])
                i-=1
        return len(nums)
    
    
    '''
    len=10
    range(1,10) so 1-9
    
    i==1
    0==0
    remove0
    [0,1,1,1,2,2,3,3,4]
    i==0
    i==1
    '''