class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            minHeap.append([x*x + y*y, x, y])
            
        heapify(minHeap)
        ans = []
        for i in range(k):
            _, x, y = heappop(minHeap)
            ans.append([x, y])
        return ans
