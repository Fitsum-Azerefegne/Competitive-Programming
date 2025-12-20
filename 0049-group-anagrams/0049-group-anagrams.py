class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       anagram_map = defaultdict(list)
       for s in strs:
        count = [0] *26
        for r in s:
            count[ord(r)-ord("a")] += 1
        key = tuple(count)
        anagram_map[key].append(s)
       return list(anagram_map.values())