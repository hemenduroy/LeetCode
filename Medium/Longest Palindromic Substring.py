class Solution:
    #Brute Force - doesn't work. "Time Limit Exceeded"
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
