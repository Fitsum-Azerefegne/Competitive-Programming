class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounter = Counter(s)
        tCounter = Counter(t)
        steps = 0
        for letter in sCounter:
            if sCounter[letter] > tCounter[letter]:
                steps += sCounter[letter] - tCounter[letter]
        return steps




