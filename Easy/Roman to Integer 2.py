class Solution:
    def romanToInt(self, s: str) -> int:
        #num=list()
        '''
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
        '''
        hashmap = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        ans=0
        #print(hashmap[s[0]])
        for i in range(len(s)-1):
            if hashmap[s[i]]<hashmap[s[i+1]]:
                ans-=hashmap[s[i]]
            else:
                ans+=hashmap[s[i]]
        ans+=hashmap[s[len(s)-1]]
        return ans