class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1 :
            return nums[0]

        self.nums = nums
        n = len(nums)
        self.memo = [-1] * n

        return self.dp(n-1)

    def dp(self, i: int) -> int:
        if i == 0:
            return self.nums[i]
        if i == 1:
            return max(self.nums[0],self.nums[1])
        if self.memo[i] == -1:
           self.memo[i] = max(self.dp(i - 1), self.dp(i - 2) + self.nums[i])
        return self.memo[i]
       