class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
            in_degree[v]

        queue = deque([node for node in in_degree if in_degree[node] == 0])
        sorted_order = []

        while queue:
            node = queue.popleft()
            sorted_order.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(sorted_order) != len(in_degree):
            return False
        return True
        
            