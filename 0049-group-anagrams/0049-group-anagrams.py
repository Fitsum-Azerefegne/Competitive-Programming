class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency_hash = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            frequency_hash[key].append(s)
        return list(frequency_hash.values())