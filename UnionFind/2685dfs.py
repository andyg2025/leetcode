from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        seen = [0]*n
        res = 0
        cur_nodes = []

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            if seen[node]:
                return 
            seen[node]=1
            cur_nodes.append(node)
            for child in graph[node]:
                dfs(child)

        def check(nodes):
            num = len(nodes)
            for node in nodes:
                if len(graph[node])!=num-1:
                    return False
            return True

        for i in range(n):
            if seen[i]:
                continue
            cur_nodes=[]
            dfs(i)
            if check(cur_nodes):
                res+=1
        return res