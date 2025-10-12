class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_height = 0
        while l < r :
            water = (r-l) * min(height[l], height[r])
            max_height = max(water,max_height)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_height
