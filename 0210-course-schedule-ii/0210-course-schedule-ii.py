class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
            in_degree[v]
        for i in range(numCourses):
            if i not in in_degree:
                in_degree[i] = 0
        
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        sorted_order = []
        while queue:
            node = queue.popleft()
            sorted_order.append(node)
            for neighbour in graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        if len(sorted_order) != len(in_degree):
            return []
        return sorted_order
        

        