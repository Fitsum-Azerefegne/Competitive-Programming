class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # truster is how many ppl he trustes
        # trustee is how many ppl trusts him
        # the judge is trusted by all except him n -1 but trust no one so truster of judge = 0 but trustee = n -1
        truster = defaultdict(int)
        trustee = defaultdict(int)
        for p1,p2 in trust:
            truster[p1] += 1
            trustee[p2] += 1
        for person in range(1,n+1):
            if trustee[person] == n-1 and truster[person] == 0:
                return person
        return -1
    