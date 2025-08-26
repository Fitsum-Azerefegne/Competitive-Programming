class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]
        graph = defaultdict(list)   
        for u, v in prerequisites:
            graph[u].append(v)  
        for i in range(numCourses):
            queue = deque([i])
            reachable[i][i] = True  # Node can reach itself
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not reachable[i][neighbor]:
                        reachable[i][neighbor] = True
                        queue.append(neighbor)
        
        return [reachable[u][v] for u, v in queries]


        