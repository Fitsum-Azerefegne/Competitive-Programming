class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {num : i for  i, num in enumerate(nums)}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hash_map:
                if hash_map[compliment] != i:
                    return [i, hash_map[compliment]]
        return []
    