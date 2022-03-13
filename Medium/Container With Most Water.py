class Solution:
  #Converge from ends
    def maxArea(self, height: List[int]) -> int:
        length=len(height)
        l,r=0,length-1
        curMax=0
        while r-l>0:
            tmp=(r-l)*min(height[l],height[r])
            curMax=max(curMax,tmp)
            if height[r]<height[l]:
                r-=1
            else:
                l+=1

        return curMax
