//DP Solution
class Solution {
    public int combinationSum4(int[] nums, int target) {
        
        HashMap<Integer,Integer> dp = new HashMap<>();
        dp.put(0,1);
        
        for (int total=1; total<=target; total++){
            dp.put(total,0);
            for (int n : nums){
                if(dp.containsKey(total-n))
                    dp.put(total,dp.get(total)+dp.get(total-n));
                    //dp[total] += dp[total-n];
            }
        }
        return dp.get(target);
    }
    
}

/*Without DP
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
*/