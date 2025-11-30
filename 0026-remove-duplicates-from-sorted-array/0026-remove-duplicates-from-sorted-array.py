class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        dd = defaultdict(int)
        for num in nums:
            if dd[num] == 0:
                nums[unique] = num
                unique += 1
            dd[num] += 1

        return unique
       