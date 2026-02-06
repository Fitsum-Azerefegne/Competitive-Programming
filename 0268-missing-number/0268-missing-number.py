class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = len(nums)
        for n in range(numbers + 1):
            if n not in nums:
                return n



        