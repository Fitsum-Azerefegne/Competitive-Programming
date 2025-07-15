class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2:
            return True
        low = 2
        high = num//2
        while low <= high:
            mid=(low + high)//2
            mid_squared = mid**2
            if mid_squared == num:
                return True
            elif mid_squared < num:
                low = mid + 1
            else:
                high = mid - 1
        return False