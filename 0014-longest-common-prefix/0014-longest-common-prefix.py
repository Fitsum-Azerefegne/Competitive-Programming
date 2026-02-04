class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first = strs[0]
        for i in range(len(first)):
            for s in strs[1:]:
                if i >= len(s) or first[i] != s[i]:
                    return res
            res += first[i]
        return res




        