class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dd = defaultdict(int)
        max_length = 0
        left = 0
        for right in range(len(s)):
            while dd[s[right]] != 0:
                dd[s[left]] -= 1
                left += 1
            max_length = max(max_length,right-left+1)
            dd[s[right]] += 1
        return max_length


