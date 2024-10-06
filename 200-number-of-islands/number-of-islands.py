class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Initialize count variable
        count = 0
        # Initialize a visited variable
        visited = set()
        # iterative code to traverse through each node in the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # explore Island when found a land
                if grid[row][col] == "1":
                    if self.explore(grid,row,col,visited):
                        count += 1
        return count
        
    def explore(self, grid, r, c, visited):
        # Check Bounds, return false
        rowBound = r < len(grid) and r >= 0
        colBound = c < len(grid[0]) and c >= 0
        if not rowBound or not colBound: return False

        # Check if Water, return false
        if grid[r][c] == "0": return False

        # Check if visited, return false
        pos = str(r) + ',' + str(c)
        if pos in visited: return False

        # Add node to visited
        visited.add(pos)

        ## Explore neighbors
        # Left
        self.explore(grid,r-1,c,visited)
        # Right
        self.explore(grid,r+1,c,visited)
        # Up
        self.explore(grid,r,c-1,visited)
        # Down
        self.explore(grid,r,c+1,visited)

        # Now that we have explored the neighbors, return True
        return True