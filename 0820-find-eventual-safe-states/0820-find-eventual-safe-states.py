class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        in_degree = defaultdict(int)
        reverse_graph = defaultdict(list)

        for i in range(len(graph)):
            for node in graph[i]:
                reverse_graph[node].append(i)
                in_degree[i] += 1
                in_degree[node]
        queue = deque([i for i in range(len(graph)) if in_degree[i] == 0])
        safe_nodes = []

        while queue:
            curr_node = queue.popleft()
            safe_nodes.append(curr_node)
            for neighbour in reverse_graph[curr_node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        return sorted(safe_nodes)