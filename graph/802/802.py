class Solution:

    def eventualSafeNodes(self, graph):
        n = len(graph)
        visited = [False]*n
        instack = [False]*n
        result = []

        for i in range(n):
            self.dfs(i, graph, visited, instack)

        for i in range(n):
            if not instack[i]:
                result.append(i)

        return result
    

    def dfs(self, node, graph, visited, instack):
        if instack[node]:
            return True

        if visited[node]:
            return False
        
        instack[node] = True
        visited[node] = True

        for n in graph[node]:
            if self.dfs(n, graph, visited, instack):
                return True
            
        instack[node] = False
        
        return False
