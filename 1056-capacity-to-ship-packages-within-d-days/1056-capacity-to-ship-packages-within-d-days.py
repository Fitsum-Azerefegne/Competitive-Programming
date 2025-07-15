class Solution:
    def canShip(self, weights: List[int], days: int, capacity:int) -> bool:
        curr_weight = 0
        day_count = 1
        for weight in weights:
            if (curr_weight + weight) > capacity:
                day_count += 1
                curr_weight = weight
                if day_count > days:
                    return False
            else:
                curr_weight += weight
        return True
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high)//2
            if self.canShip(weights, days, mid):
                high = mid
            else:
                low = mid +1
        return low
        