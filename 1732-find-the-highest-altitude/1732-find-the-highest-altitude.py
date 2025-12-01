class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        original = [0] * (len(gain) + 1)
        for i in range(1,len(gain)+1):
            original[i] = original[i-1] + gain[i-1]
        return max(original)

        
        