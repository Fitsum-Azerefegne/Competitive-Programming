class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        happy_children = 0
        g_pointer = s_pointer = 0
        while (g_pointer < len(g)) and (s_pointer < len(s)):
            if s[s_pointer] >= g[g_pointer]:
                happy_children += 1
                g_pointer += 1
            s_pointer +=1
        return happy_children
