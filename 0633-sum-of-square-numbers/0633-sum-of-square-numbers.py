import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start, end = 0, int(math.isqrt(c))
        while start <= end:
            summ = ((start**2) + (end**2)) 
            if summ == c :
                return True
            elif summ > c:
                end -= 1
            else:
                start += 1
        return False