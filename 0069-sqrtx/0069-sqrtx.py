class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        low = 2
        high = x//2
        while low <= high:
            mid=(low + high)//2
            mid_squared = mid**2
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                low = mid + 1
            else:
                high = mid - 1
        return high