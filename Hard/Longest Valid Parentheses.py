class Solution:
    # time - O(n), space - O(n)
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        res = 0
        
        for i in range(len(s)):
            
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
                
        return res

'''
class Solution:
    # time - O(n), space - O(1)
    def longestValidParentheses(self, s: str) -> int:

        open,close=0,0
        
        length=len(s)
        res=0
        
        for i in range(length):
            if s[i]=='(':
                open+=1
            else:
                close+=1
                
            if open==close:
                res=max(res,open+close)
            if close>open:
                #reset
                open,close=0,0
              
        open,close=0,0
        for i in range(length-1,-1,-1):
            if s[i]=='(':
                open+=1
            else:
                close+=1
                
            if open==close:
                res=max(res,open+close)
            if close<open:
                #reset
                open,close=0,0
                
        return res
                
'''
