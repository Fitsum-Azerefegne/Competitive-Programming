class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles 
        full = numBottles
        while full >= numExchange:
            full -= numExchange
            drank += 1
            numExchange += 1
            full += 1 
        
        return drank

