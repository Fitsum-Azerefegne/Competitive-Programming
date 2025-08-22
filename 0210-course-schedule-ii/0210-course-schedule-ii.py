class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        courses = []
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
            in_degree[v]

        queue = deque([v for v in range(numCourses) if in_degree[v] == 0])
        while queue:
            current_course = queue.popleft()
            courses.append(current_course) 
            
            for next_course in graph[current_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        if len(courses) != numCourses:
            return []
        return courses
        