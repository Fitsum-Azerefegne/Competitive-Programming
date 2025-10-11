class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()  
        chemistry = 0
        left = 0
        right = len(skill) -1
        probable = skill[right] + skill[left]
        while left < right:
            if (skill[right]+ skill[left]) != probable:
                return -1
            chemistry += (skill[left]*skill[right])
            left += 1
            right -= 1
        return chemistry

        