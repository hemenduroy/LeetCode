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
  '''
  def reverse(self, x: int) -> int:
        diglist=[]
        k=1
        if x<0:
            x*=-1
            k=0
        while True:
            digit=x%10
            x//=10
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
  '''
  #Don't need an array. Still uses 64 bit integers
  '''
  def reverse(self, x: int) -> int:
        res=0
        k=1
        if x<0:
            x*=-1
            k=0
        while True:
            digit=x%10
            x//=10
            res*=10
            res+=digit
            if x==0:
                break

        if res>2**31-1:
            return 0
        if k==1:
            return res
        else:
            return res*-1
  '''
  #before multiplying by 10, check if res exceeds MAX//10. also, check if res==MAX//10 and adding last digit would cause overflow
  #same for MIN
  #math.fmod used because using % with negative numbers in python returns unexpected values
  def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        res=0
        while x:
            digit=int(math.fmod(x,10))
            x=int(x/10)

            if (res>MAX//10 or (res==MAX//10 and digit>=MAX%10)):
                return 0
            if (res<MIN//10 or (res==MIN//10 and digit<=MIN%10)):
                return 0
            res=res*10+digit
        return res
