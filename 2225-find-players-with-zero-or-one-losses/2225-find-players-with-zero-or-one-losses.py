class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = []
        losses = defaultdict(int)
        for a, b in matches:
            if a not in losses:
                losses[a] = 0
            losses[b] += 1
        winner = [n for n in losses if losses[n] == 0]
        loser = [n for n in losses if losses[n] == 1 ]
        answer = [sorted(winner), sorted(loser)]
        return answer   