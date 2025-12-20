class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hash_map = defaultdict(int)
        steps = 0
        for letter in s:
            hash_map[letter] += 1
        for letter in t:
            hash_map[letter] -= 1
            if hash_map[letter] < 0:
                steps += 1
                hash_map[letter] += 1
        return steps
        