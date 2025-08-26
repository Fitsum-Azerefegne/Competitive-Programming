class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Initialize ancestors as sets for each node
        ancestors = [set() for _ in range(n)]
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()     
            for neighbor in graph[node]:
                ancestors[neighbor] |= ancestors[node]
                # Take all the elements from both sets and combine them into a new set, then assign it back to ancestors[neighbor]
                ancestors[neighbor].add(node)
                
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]