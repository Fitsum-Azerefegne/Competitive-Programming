class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def in_bound(r,c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])

        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = color

        while queue:
            x, y = queue.popleft()
            for i,j in dir:
                newx, newy = x + i, y + j
                if in_bound(newx, newy) and image[newx][newy] == original_color:
                    image[newx][newy] = color
                    queue.append((newx,newy))

        return image

        