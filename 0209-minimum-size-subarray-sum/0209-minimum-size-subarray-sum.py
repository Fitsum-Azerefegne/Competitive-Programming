class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minimal_length = float("inf")
        left = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                minimal_length = min(minimal_length, (right-left+1))
                curr_sum -= nums[left]
                left += 1
        if minimal_length != float("inf"):
            return minimal_length
        else:
            return 0 
            
            


