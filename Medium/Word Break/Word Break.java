class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
        int length = s.length();
        boolean[] dp = new boolean[length+1];
        dp[length]=true;
        
        for(int i = length-1;i>=0;i--){
            for(int j=0;j<wordDict.size();j++){
                try{
                    String word = wordDict.get(j);
                    //System.out.println(s.substring(i,i+word.length()));
                    if(s.substring(i,i+word.length()).equals(word)){
                        dp[i]=dp[i+word.length()];
                        if(dp[i])
                            break;
                    }
                }
                catch(Exception e){
                    continue;
                }
            }
        }
        return dp[0];
    }
}