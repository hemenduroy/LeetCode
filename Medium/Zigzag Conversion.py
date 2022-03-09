class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        sz=[""]*numRows
        cur=-1
        flag=0
        for i in s:
            if cur==numRows-1:
                flag=1
            if cur==0:
                flag=0
            if flag==0:
                cur+=1
            else:
                cur-=1
            sz[cur]+=i
        return "".join(sz)
