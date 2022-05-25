class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        starts=[]
        rows=len(grid)
        cols=len(grid[0])
        found_fresh=False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2: #rotten
                    starts.append((i,j))
                if grid[i][j]==1:
                    found_fresh=True
        
        if not found_fresh:
            return 0
        
        #print(starts)
        return self.bfs(starts,grid,rows,cols)
        
    
    def isInBound(self,x,y,rows,cols):
        return x in range(rows) and y in range(cols)
    
    def bfs(self,queue,grid,rows,cols):
        
        visited=set()
        for (x,y) in queue:
            visited.add((x,y))
        
        ops=[(0,1),(1,0),(0,-1),(-1,0)] #up right down left
        
        curr=len(queue)
        level=0
        while queue:
            
            if curr==0: #finished current level
                level+=1 #elapse a minute
                curr=len(queue) #set number of nodes to check in next minute
                
            x,y=queue.pop(0)
            curr-=1
            
            for dx,dy in ops:
                posX=x+dx
                posY=y+dy
                

                if self.isInBound(posX,posY,rows,cols):
                    if (posX,posY) not in visited and grid[posX][posY]==1:
                        grid[posX][posY]=2 #make fresh orange rotten
                        queue.append((posX,posY))
                        visited.add((posX,posY))
                        
        
        #bfs complete. check if fresh oranges are remaining
        #if they are, return -1. else return count
        
        for i in grid:
            for j in i:
                if j==1:
                    return -1
                
        return level #nth level = n minutes elapsed
            
