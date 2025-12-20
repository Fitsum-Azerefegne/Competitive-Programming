class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        hash_map = defaultdict(int)
        
        for letter in s:
            hash_map[letter] += 1
        
        for letter in t:
            hash_map[letter] -= 1
            if hash_map[letter] < 0:
                return False 
        return True   
