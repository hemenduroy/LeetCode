class Solution {
    public int mySqrt(int x) {
        
        if (x<=1){
            return x;
        }
        long start=0;
        long end=x;
        long mid=0;
        while (start<=end){
            //System.out.println(mid+'\n');
            mid=(start+end)/2;
            if(Math.pow(mid,2) == x)
                return (int)mid;
            if (Math.pow(mid,2) > x)
                end=mid-1;
            else
                start=mid+1;
        }
        
        if (Math.pow(mid,2) > x)
            return (int)mid-1;
        return (int)mid;
    }
}
