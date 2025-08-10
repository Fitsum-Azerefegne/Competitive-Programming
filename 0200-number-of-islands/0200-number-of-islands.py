class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def in_bound(r,c):
            return 0<=r< len(grid) and 0<=c<len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    queue = deque()
                    queue.append((i, j))
                    grid[i][j] = "0"  
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in dir:
                            nx, ny = x + dx, y + dy
                            if in_bound(nx,ny) and grid[nx][ny] == "1":
                                queue.append((nx, ny))
                                grid[nx][ny] = "0"
        return islands
                