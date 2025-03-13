class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        stack = [0]
        parents = {0:-1}

        while stack:
            node = stack.pop()
            for child in graph[node]:
                if child == parents[node]:
                    continue
                if child in parents:
                    return False
                stack.append(child)
                parents[child]=node
        
        return len(parents)==n