class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum_of_all = 0
        n = len(nums)
        for index, num in enumerate(nums, start = 1):
            if n % index == 0:
                sum_of_all += (num ** 2)
        return sum_of_all