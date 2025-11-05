class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
    
        output = []
        pre_start = intervals[0][0]
        pre_end = intervals[0][1]

        for start, end in intervals[1:]:  
            if start <= pre_end: 
                pre_end = max(pre_end, end)
            else:
                output.append([pre_start, pre_end])
                pre_start = start
                pre_end = end

        output.append([pre_start, pre_end])
        return output
        
 