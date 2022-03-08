class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre=""
        cur=""
        count=0
        if len(strs)==0:
            return ""
        for j in range(len(min(strs,key=len))):
            cur=strs[0][0:j+1]
            for i in strs:
                if i.startswith(cur):
                    count+=1
                else:
                    return pre
                if count==len(strs):
                    count=0
                    pre=cur
            
        return pre