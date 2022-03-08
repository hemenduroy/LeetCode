class Solution:
    def romanToInt(self, s: str) -> int:
        num=list()
        for i in s:
            if i=='I':
                num.append(1)
            elif i=='V':
                num.append(5)
            elif i=='X':
                num.append(10)
            elif i=='L':
                num.append(50)
            elif i=='C':
                num.append(100)
            elif i=='D':
                num.append(500)
            elif i=='M':
                num.append(1000)

        ans=0
        for i in range(len(num)-1):
            if num[i]<num[i+1]:
                ans-=num[i]
            else:
                ans+=num[i]
        ans+=num[len(num)-1]    
        return ans