class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        start = 0
        end = len(skill) - 1
        skills = skill[0] + skill[end]
        while start < end:
            if skills != skill[start] + skill[end]:
                return -1
            chemistry += (skill[start]* skill[end])
            start += 1
            end -= 1
        return chemistry
      