class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = defaultdict(int)
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u) # we reverse it so we can have terminal ones with no in degree
                in_degree[u] += 1
                in_degree[v]
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)   
        safe_states = []
        while queue:
            node = queue.popleft()
            safe_states.append(node)
            for neigh in reverse_graph[node]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)
        return sorted(safe_states)
