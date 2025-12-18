class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        dd = defaultdict(int)
        left = 0
        for right in range(len(s)):
            dd[s[right]] += 1
            while dd[s[right]] > 1: 
                dd[s[left]] -= 1
                left += 1
            longest_length = max(longest_length,right - left + 1)
        return longest_length



       

