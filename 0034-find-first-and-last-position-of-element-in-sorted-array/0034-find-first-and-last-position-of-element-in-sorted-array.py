class Solution:
    def findFirst(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low 
    def findLast(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

        return high
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findFirst(nums,target)
        last = self.findLast(nums,target)
        if first <= last:
            return [first,last]
        else:
            return[-1,-1]
        
    