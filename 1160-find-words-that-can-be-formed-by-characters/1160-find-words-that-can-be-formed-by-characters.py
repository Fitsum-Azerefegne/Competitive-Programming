class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_hash = defaultdict(int)
        output = 0
        for ch in chars:
            chars_hash[ch] += 1 
        for word in words:
            hash_map = defaultdict(int)
            valid = True
            for char in word:
                hash_map[char] += 1
            for char in word: 
                if char not in chars_hash or hash_map[char] > chars_hash[char]:
                    valid = False
                    break
            if valid:
                output += len(word)
        return output
            

        