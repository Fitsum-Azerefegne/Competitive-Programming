class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        happy_children = 0
        for i in range(min(len(s),len(g))):
            if g[i] <= s[i]:
                happy_children += 1
        return happy_children