class Solution:

    def checkWin(self, grid: List[List[int]], player: int) -> bool:


        h=len(grid)
        w=len(grid[0])


        #horizontals
        for i in range(h):
            for j in range(w-3):

                if grid[i][j]==grid[i][j+1]==grid[i][j+2]==grid[i][j+3]==player:
                    print('horizontal')
                    return True


        #verticals
        for i in range(h-3):
            for j in range(w):

                if grid[i][j]==grid[i+1][j]==grid[i+2][j]==grid[i+3][j]==player:
                    print('vertical')
                    return True


        #diagonal \
        for i in range(h-3):
            for j in range(w-3):

                if grid[i][j]==grid[i+1][j+1]==grid[i+2][j+2]==grid[i+3][j+3]==player:
                    print('diagonal \\')
                    return True


        #diagonal /
        for i in range(3,h):
            for j in range(w-3):

                if grid[i][j]==grid[i-1][j+1]==grid[i-2][j+2]==grid[i-3][j+3]==player:
                    print('diagonal /')
                    return True

        return False
