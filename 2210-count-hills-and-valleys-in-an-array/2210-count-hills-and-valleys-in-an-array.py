class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        clean_nums = []
        for num in nums:
            if not clean_nums or clean_nums[-1] != num:
                clean_nums.append(num)
        hill_valley = 0
        for i in range(1, len(clean_nums)-1):
            if clean_nums[i] > clean_nums[i+1] and clean_nums[i-1] < clean_nums[i]:
                hill_valley += 1
            elif clean_nums[i] < clean_nums[i+1] and clean_nums[i-1] > clean_nums[i]: 
                hill_valley += 1
        return hill_valley