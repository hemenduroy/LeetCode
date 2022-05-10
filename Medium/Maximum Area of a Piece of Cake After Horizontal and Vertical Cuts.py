class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        height=0 #max height
        for i in range(1,len(horizontalCuts)):
            height=max(height,horizontalCuts[i]-horizontalCuts[i-1])
            
        width=0 #max width
        for i in range(1,len(verticalCuts)):
            width=max(width,verticalCuts[i]-verticalCuts[i-1])
            
        return height*width % (10**9+7)
