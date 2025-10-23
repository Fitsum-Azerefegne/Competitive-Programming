class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumLeft = [0] * n
        sumRight = [0] * n
        for i in range(n):
            sumLeft[i] = sum(nums[:i])
            sumRight[i] = sum(nums[i+1:])
            if sumRight[i] == sumLeft[i]:
                return i
        return -1
        