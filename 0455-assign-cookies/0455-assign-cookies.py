class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        happy_children = 0
        g_point = s_point = 0
        while (g_point<len(g) and s_point<len(s)):
            if s[s_point] >= g[g_point]:
                happy_children += 1
                g_point += 1
            s_point +=1
        return happy_children