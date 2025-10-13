class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums) -1
            while l < r:
                current_sum = a + nums[l] + nums[r]
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum                   
                if current_sum > target:
                    r -= 1
                elif current_sum < target:
                    l += 1
                else:
                    return closest
        return closest


        