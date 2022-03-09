class Solution:
    #Brute Force - doesn't work. "Time Limit Exceeded"
    '''
    def longestPalindrome(self, s: str) -> str:
        sub=''
        res=''
        for j in range(len(s)):
            for i in range(len(s)):
                sub=s[j:i+1]
                if sub==sub[::-1] and len(sub)>len(res):
                    res=sub
                if len(res)>len(s)-j:
                    return res
        return res
    '''
    #expand from center
    def longestPalindrome(self, s: str) -> str:
        res=""
        length_res=0

        #odd
        for i in range(len(s)):
            l,r=i,i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if (r-l+1)>length_res:
                    res=s[l:r+1]
                    length_res=r-l+1
                l-=1
                r+=1
        #even
        for i in range(len(s)):
            l,r=i,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if (r-l+1)>length_res:
                    res=s[l:r+1]
                    length_res=r-l+1
                l-=1
                r+=1

        return res
