class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        graph = [set() for _ in range(n)]

        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        print(graph)

        leaves = [ node for node in range(n) if len(graph[node])==1 ]

        num_left_node = n
        while n>2:
            n-=len(leaves)
            new_leaves = []
            for leaf in leaves:
                pre = graph[leaf].pop()
                graph[pre].remove(leaf)
                if len(graph[pre])==1:
                    new_leaves.append(pre)

            leaves = new_leaves[:]

        return leaves