class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for ppl in range(1,n+1):
           res = (res + k) % ppl 
        return res + 1