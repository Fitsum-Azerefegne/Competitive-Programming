class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_hash = defaultdict(int)
        for char in s:
            char_hash[char] += 1
        for index,char in enumerate(s):
            if char_hash[char] == 1:
                return index
        return -1
        