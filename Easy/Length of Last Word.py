class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for i in s[::-1]:
            if i is not ' ':
                count+=1
            if count>0 and i == ' ':
                break
        return count
