class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        

        intervals.sort(key=lambda x: x[1])
        
        output = 0 
        pre_end = intervals[0][1] 
        for start, end in intervals[1:]:
            if start < pre_end:  
                output += 1 
            else:
                pre_end = end  

        return output
        