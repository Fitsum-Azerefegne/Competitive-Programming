class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_ones = sum(nums)  
        max_score = 0
        left_zeros = 0
        indices = []

        for i in range(len(nums) + 1):
            score = left_zeros + (total_ones - (i - left_zeros))
            if score > max_score:
                max_score = score
                indices = [i]
            elif score == max_score:
                indices.append(i)

            if i < len(nums) and nums[i] == 0:
                left_zeros += 1

        return indices