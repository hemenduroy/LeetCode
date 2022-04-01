class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        int i=0,j=0;
        ArrayList<Integer> res= new ArrayList<>();
        while(i<m || j<n){
            if (i>=m){
                //System.out.println(i+" "+j);
                res.add(nums2[j]);
                j++;
                continue;
            }
            if (j>=n){
                res.add(nums1[i]);
                i++;
                continue;
            }
            if(nums1[i]<=nums2[j]){
                res.add(nums1[i]);
                    i++;
            }
            else{
                res.add(nums2[j]);
                    j++;
            }
            //System.out.println(i<m || j<n);
            //System.out.println(j);
        }
        for(int k=0; k<m+n;k++)
            nums1[k]=res.get(k);
    }
}
