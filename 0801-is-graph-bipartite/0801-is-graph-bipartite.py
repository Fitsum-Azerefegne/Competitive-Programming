class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        for i in range (len(graph)):
            if color[i] == -1:
              queue = deque()
              queue.append((i))
              color[i] = 1  
              while queue:
                  n = queue.popleft()
                  for neigh in graph[n]:
                    if color[neigh] == -1:
                          if color[n]== 1:
                            color[neigh] = 0
                          else:
                            color[neigh] = 1
                          queue.append((neigh))
                    elif color[neigh] == color[n]:
                            return False  
        return True


