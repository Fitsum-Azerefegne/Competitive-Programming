class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
            if hashmap[n] > 1:
                return True
        return False
        