class Solution(object):
    def minPathSum(self, grid):
        r, c = len(grid), len(grid[0])
        
        if r==1 and c==1:
            return grid[0][0]
        
        heap = [(grid[0][0], (0,0))]
        visit = set()
        while heap:
            s, (i, j) = heapq.heappop(heap)
            if (i,j) in visit: continue    # <--- this is the key to avoid TLE
            visit.add((i,j))
            for x, y in ((i+1, j), (i,j+1)):
                if x<r and y<c:
                    s1 = s + grid[x][y]
                    heapq.heappush(heap, (s1, (x,y)))
                    if x==r-1 and y==c-1:
                        return s1


'''
### Without heap - time limit exceeded
class Solution(object):
    def minPathSum(self, grid):
        r, c = len(grid), len(grid[0])
        
        if r==1 and c==1:
            return grid[0][0]
        
        heap = [(grid[0][0], (0,0))]
        visit = set()
        
        dists=[]
        while heap:
            #s, (i, j) = heapq.heappop(heap)
            s, (i, j) = heap.pop(0)
            #if (i,j) in visit: continue    # <--- this is the key to avoid TLE
            #visit.add((i,j))
            for x, y in ((i+1, j), (i,j+1)):
                if x<r and y<c:
                    s1 = s + grid[x][y]
                    #heapq.heappush(heap, (s1, (x,y)))
                    heap.append((s1, (x,y)))
                    if x==r-1 and y==c-1:
                        #return s1
                        dists.append(s1)
        #print(dists)
        return min(dists)
'''
