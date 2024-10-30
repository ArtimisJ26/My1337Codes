class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        counter = 0

        def explore(r, c):
            if r > len(grid)-1 or r < 0 or c < 0 or c > len(grid[0])-1:
                return

            if grid[r][c] == "0":
                return
            
            location = str(r) + "," + str(c)
            if location in visited:
                return
            
            visited.add(location)
            # print(visited)

            # up
            explore(r-1,c)
            # down
            explore(r+1,c)
            # left
            explore(r,c-1)
            # right
            explore(r,c+1)

        # explore(0,0)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                location = str(row) + "," + str(col)
                if location not in visited:
                    if grid[row][col] == "1":
                        counter += 1
                    explore(row,col)
                    

        return counter