# this problem should be solved by unionFind, but it is more easier to do it using the greedy.
# Since greedy is not the common way to deal with such problems, dfs, bfs and unionfind should be the best used way


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        seen = [0]*n
        res = 0

        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def check(node):
            if seen[node]:
                return False
            seen[node] = 1
            graph[node].add(node)
            for child in graph[node]:
                seen[child]=1
                graph[child].add(child)
                if graph[node] != graph[child]:
                    return False
            
            return True

        for i in range(n):
            if check(i):
                res+=1
        
        return res