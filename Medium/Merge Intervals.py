class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        i=0
        
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                combined=[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                intervals=intervals[:i] + [combined] + intervals[i+2:]
                i-=1
            i+=1
        return intervals
