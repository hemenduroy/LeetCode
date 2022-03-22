class Solution {
    public int searchInsert(int[] nums, int target) {
        /*O(n)
        int i=0
        for(i=0;i<nums.length;i++){
            if ((nums[i]==target) || (nums[i]>target)){
                break;
            }
        }
        return i;
        */
        //binary search 0(logn)
        int start=0,end=nums.length-1;
        int mid=0;
        while(start<=end){
            mid=(start+end)/2;
            if (nums[mid]==target){
                return mid;
            }
            else if (nums[mid]>target){
                end=mid-1;
            }
            else{
                start=mid+1;
            }
        }//end while
        return start; // start will always have the correct position if element is not found. dont need the if conditions.
        /*
        if(end<mid){
                if(end==-1){
                    return 0;
                }
                else{
                    return mid;
                }
            }
            else{
                return start;
            }
        */
    }
}
