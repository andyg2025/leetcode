from typing import List
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:        
        graph = [ set() for _ in range(n)]
        for [a,b] in edges:
            graph[a].add(b)
            graph[b].add(a)

        result = [0]*n

        que = deque()
        
        for i in range(n):
            if len(graph[i]) == 1:
                que.append(i)
            if not graph[i]:
                return False
        
        while que:
            node = que.popleft()
            for e in graph[node]:
                graph[e].remove(node)
                result[node]=1
            if len(graph[e])==1:
                que.append(e)
            if not graph[e] and len(que)>1:
                    print(e)
                    print(que)
                    return False

        print(result)
        
        return sum(result)==(n-1)
    

def main():
    edges = [[0,1],[0,2],[0,3],[1,4]]
    n=5
    s = Solution()
    result = s.validTree(n, edges)
    print(result)

if __name__ == "__main__":
    main()