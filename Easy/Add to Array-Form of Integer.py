class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        length=len(num)
        carry=0
        for i in range(length-1,-1,-1):
            num[i],carry= (num[i] + k%10 + carry)%10 , (num[i] + k%10 + carry)//10
            k=k//10
            
        rem = k + carry
        while rem>0:
            num=[rem%10]+num
            rem=rem//10
        return num
