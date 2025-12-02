class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        curr_sum = 0
        left = 0
        maxsum = 0
        for right in range(len(nums)):

            while nums[right] in seen:
                curr_sum -= nums[left]
                seen.remove(nums[left])
                left += 1

            seen.add(nums[right])
            curr_sum += nums[right]
            if right - left + 1 > k:
                curr_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            if right - left + 1 == k :
                maxsum = max(maxsum, curr_sum)
        return maxsum
