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
        
        #print(visited)
        ops=[(0,1),(1,0),(0,-1),(-1,0)]
        
        curr=len(queue)
        level=0
        while queue:
            
            if curr==0:
                level+=1
                curr=len(queue)
                
            x,y=queue.pop(0)
            curr-=1
            
            for dx,dy in ops:
                #print(dx,dy)
                posX=x+dx
                posY=y+dy
                

                if self.isInBound(posX,posY,rows,cols):
                    #print(posX,posY)
                    if (posX,posY) not in visited and grid[posX][posY]==1:
                        #print(x,y)
                        #print(posX,posY)
                        grid[posX][posY]=2
                        queue.append((posX,posY))
                        visited.add((posX,posY))
                        
        
        #bfs complete. check if fresh oranges are remaining
        #if they are, return -1. else return count
        
        #print(grid)
        for i in grid:
            for j in i:
                if j==1:
                    return -1
                
        #print(extra)
        return level
            
