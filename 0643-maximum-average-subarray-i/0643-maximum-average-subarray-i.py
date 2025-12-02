class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_average = window_sum /k
        for end in range(k,len(nums)):
            window_sum += nums[end]
            window_sum -= nums[end - k]
            max_average = max(max_average,(window_sum/k))
        return max_average
            



       