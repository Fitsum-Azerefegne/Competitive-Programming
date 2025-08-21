class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
            in_degree[v]

        queue = deque([v for v in range(numCourses) if in_degree[v] == 0])
        taken_courses = 0
        while queue:
            current_course = queue.popleft()
            taken_courses += 1  
            
            for next_course in graph[current_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return taken_courses == numCourses