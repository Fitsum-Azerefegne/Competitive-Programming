class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1
        return [ key for key, value in hash_map.items() if value > 1]
        