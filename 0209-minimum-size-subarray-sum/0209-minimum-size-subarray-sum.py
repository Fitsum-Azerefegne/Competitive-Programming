class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        subarray_sum = 0
        output = float("inf")
        for end in range(len(nums)):
            subarray_sum += nums[end]
            while subarray_sum >= target:
                output = min(output, end - start + 1)
                subarray_sum -= nums[start]
                start += 1
        return 0 if output == float("inf") else output