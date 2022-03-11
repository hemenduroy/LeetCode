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
  #Still stores 64 bit numbers in edge cases
  def reverse(self, x: int) -> int:
        diglist=[]
        k=1
        if x<0:
            x*=-1
            k=0
        while True:
            digit=x%10
            x-=digit
            x/=10
            diglist.append(digit)
            if len(diglist)>10:
                return 0
            if x==0:
                break
            diglist = [i * 10 for i in diglist]

        res=int(sum(diglist))
        print(res)
        if res>2**31-1:
            return 0
        if k==1:
            return res
        else:
            return res*-1
