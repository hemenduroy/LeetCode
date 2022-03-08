class Solution:
    def isValid(self, s: str) -> bool:
        blist=list()
        for i in s:
            if len(blist)==0 and (i==')' or i==']' or i=='}'):
                return False    
            if i=='(':
                blist.append('r')
            elif i=='{':
                blist.append('c')
            elif i=='[':
                blist.append('s')
            elif blist[-1]=='r' and (i==']' or i=='}'):
                return False
            elif blist[-1]=='c' and (i==']' or i==')'):
                return False
            elif blist[-1]=='s' and (i==')' or i=='}'):
                return False
            else:
                blist = blist[:-1]
        if len(blist)!=0:
            return False
        else:
            return True