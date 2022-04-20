class Solution:
    def calculate(self, s: str) -> int:
        
        stack=[]
        
        def myEval(string):
            string=string.replace(' ','').replace('--','+')
            ops=re.split('([+-])',string)

            res=0
            add=True
            for i in range(len(ops)):
                if ops[i]=='+':
                    add=True
                    continue
                if ops[i]=='-':
                    add=False
                    continue
                    
                if ops[i].isdigit():
                    if add:
                        res+=int(ops[i])
                    else:
                        res-=int(ops[i])
               
            return res
        
        i=-1
        while i< len(s):
            if ')' not in s:
                return myEval(s)
            i+=1
            if s[i]=='(':
                stack.append(i)
                
            if s[i]==')':
                
                str2eval=s[stack[-1]+1 : i]
                res=myEval(str2eval)
                
                s=s[:stack[-1]]+str(res)+s[i+1:len(s)]
                stack.pop()
                i-=(len(str2eval)+1)
                
