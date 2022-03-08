class Solution {
    public int strStr(String haystack, String needle) {
        
        if (needle.isEmpty()){
            return 0;
        }
        int i;
        for(i=0;i<haystack.length();i++){
            if(i+needle.length()>haystack.length()){
                break;
            }
            if(haystack.substring(i,i+needle.length()).equals(needle))
                return i;
            //System.out.println(haystack.charAt(i));
        }
        return -1;
        //return haystack.indexOf(needle,0);
    }
}