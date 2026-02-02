class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if nums[i] == 0 and maxReach <= i and i < len(nums)-1:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True      