class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = 0
        true_x = x
        while x > 0 :
            d = x % 10      
            reversed_x = (reversed_x*10) + d 
            x = x // 10
        return (reversed_x == true_x)
        