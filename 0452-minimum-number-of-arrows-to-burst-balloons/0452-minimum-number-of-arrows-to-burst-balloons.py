class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[0])
    
        arrows = 1

        pre_end = points[0][1]
        for start, end in points[1:]:  
            if start <= pre_end: 
                pre_end = min(pre_end, end)
            else:
                pre_end = end
                arrows += 1

        return arrows
        
 