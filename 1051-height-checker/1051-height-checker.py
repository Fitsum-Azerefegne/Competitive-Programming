class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        checker = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                checker += 1
        return checker

       