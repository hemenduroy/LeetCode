class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        height = len(s)
        while '**' in p:
            p=p.replace('**','*')
        width = len(p)
        
        if width==0:
            return height==0
        
        T = [[False for i in range(width+1)] for j in range(height+1)]
        
        T[0][0]=True
        T[0][1] = p[0]=='*'
        
        for i in range(1,height+1):
            for j in range(1, width+1):
                if s[i-1]==p[j-1] or p[j-1]=='?': # current char matches. Entire string matches if it had matched before this.
                    T[i][j] = T[i-1][j-1]
                elif p[j-1]=='*':
                    T[i][j]=T[i-1][j] or T[i][j-1]
                    # T[i-1][j] - * matches current char of s
                    # so s till previous char must match with p
                    # T[i][j-1] - * matches with empty sequence 
                    # that means s till curent char matches p till previous char 
                    # because current char of p i.e., * matches with empty string


        return T[height][width]
'''
TLE
def isMatch(s: str, p: str) -> bool: 
   return re.match("^" + p.replace("*",".*").replace("?",".") + "$", s)
'''
