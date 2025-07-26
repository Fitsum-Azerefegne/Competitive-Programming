class Solution:
    def binary_search(self,heaters, house):
        left, right = 0, len(heaters) - 1
        while left <= right:
            mid = (left + right) // 2
            if heaters[mid] < house:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0
        for house in houses:
            idx = self.binary_search(heaters,house)
            left_heater_dist = float('inf') 
            right_heater_dist = float("inf")
            if idx > 0:
                left_heater_dist = house - heaters[idx - 1]
            if idx < len(heaters):
                right_heater_dist = heaters[idx] - house
            
            min_distance = min(left_heater_dist, right_heater_dist)
            
            max_radius = max(max_radius, min_distance)

        return max_radius

