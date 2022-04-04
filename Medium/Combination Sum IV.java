//Without DP
class Solution {
    int count=0;
    public int combinationSum4(int[] nums, int target) {
        
        return recurFunc(nums,0,target);
        
    }
    
    public int recurFunc(int[] nums, int sum, int target){
        if (sum==target){
            count++;
            return count;
        }
        if (sum>target)
            return count;
            
        for(int i : nums)
            count=recurFunc(nums,i+sum,target);
        
        return count;
    }
}
