class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1  
        missing_count = 0 
        index = 0  
        while missing_count < k:
            if index < len(arr) and arr[index] == num:
                index += 1
            else: 
                missing_count += 1  
                if missing_count == k:
                    return num           
            num += 1  
        return num



