class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_area = 0
        def in_bound(r,c):
            return 0<=r< len(grid) and 0<=c<len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    queue = deque()
                    queue.append((i,j))
                    area = 0
                    while queue:
                        x, y = queue.popleft()
                        area +=1
                        for dx, dy in dir:
                            nx = x + dx
                            ny = y + dy
                            if in_bound(nx,ny) and grid[nx][ny] == 1:
                                queue.append((nx,ny))
                                grid[nx][ny] = 0
                    max_area = max(max_area,area)
        return max_area
                            
                    

        