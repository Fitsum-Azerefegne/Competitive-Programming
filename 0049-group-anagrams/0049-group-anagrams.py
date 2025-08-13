class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # Create a key by sorting the string
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
        print(anagram_map)
        
        return list(anagram_map.values())