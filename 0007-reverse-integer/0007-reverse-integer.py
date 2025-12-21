class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1  
        x *= sign # make it abs value
        
        reversed_num = 0
        
        while x != 0:
            digit = x % 10  
            x //= 10  
            
            # Check overflow
            if reversed_num > (2**31 - 1) // 10 or (reversed_num == (2**31 - 1) // 10 and digit > 7):
                return 0
            
            reversed_num = reversed_num * 10 + digit  
        
        return sign * reversed_num  