class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxMins = 0
        rotten = deque()
        fresh = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rotten.append([row,col])
                elif grid[row][col] == 1:
                    fresh += 1

        while rotten and fresh > 0:
            maxMins += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()

                for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    x = r + dx
                    y = c + dy

                    if x >= 0 and y >= 0 and x < ROWS and y < COLS and grid[x][y] == 1:
                        grid[x][y] = 2
                        rotten.append([x,y])
                        fresh -= 1
                
        if fresh > 0:
            return -1
        
        return maxMins