class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes, key=lambda x: x[1], reverse=True)
        units=0
        i=0
        while truckSize>0 and i<len(boxTypes):
            for j in range(boxTypes[i][0]):
                truckSize-=1
                units+=boxTypes[i][1]
                if truckSize==0:
                    break
            i+=1
                
        return units
