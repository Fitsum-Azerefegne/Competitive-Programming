class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # the four directions the oranges rotten
        dir = [(1,0), (0,1), (0,-1), (-1,0)]
        # check if the orange is in bound
        def in_bound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        queue = deque()
        # queue to store the current i,j and minutes spent
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append(((i,j),0))
                    grid[i][j] = 0
        # we add in the queue all the rotton ones and change them to 0
        mx = 0
        while queue:
            coord, time = queue.popleft()
            for xi, xj in dir:
                # check by all four directions from the rotten
                newi, newj = coord[0] + xi, coord[1] + xj
                if in_bound(newi, newj) and grid[newi][newj] == 1:
                    # if the new one is inbound and valued one then we add it to the queue cause it's rotten
                    # and append to the queue so we can check the next
                    queue.append(((newi, newj), time+1))
                    grid[newi][newj] = 0
                    # the time value does not change still mx takes the max from the two
                    mx = max(time+1, mx)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        # lastly if there is an orange by anychance that has not gotton rotten it returns -1
        return mx


                        
