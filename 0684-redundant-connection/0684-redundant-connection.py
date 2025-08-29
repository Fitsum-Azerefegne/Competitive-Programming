class Unionfind:
    def __init__(self):
        self.parent = {}
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.parent[rooty] = rootx
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = Unionfind()

        for u, v in edges:
            if uf.find(u) == uf.find(v):
              return [u,v]
            uf.union(u,v)
        return []  