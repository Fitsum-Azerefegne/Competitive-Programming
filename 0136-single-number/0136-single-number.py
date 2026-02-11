class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        for num in nums:
            dd[num] += 1
        for num in nums:
            if dd[num] == 1:
                return num
            