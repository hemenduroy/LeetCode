class Solution:
  #Using str()
  #Not allowed because 7 can't store a 64 bit integer at line 11
  '''
    def reverse(self, x: int) -> int:
        k=1
        if x<0:
            x*=-1
            k=0
        
        y=int(str(x)[::-1])
        if k==0:
            y*=-1
        if y>2147483647 or y<-2147483647:
            return 0
        else:
            return y
  '''
            
