from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for index, letter in enumerate(s):
            if count[letter] == 1:
                return index
        return -1
        