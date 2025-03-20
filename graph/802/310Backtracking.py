# Time Limit Exceeded

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        grap = [set() for _ in range(n)]
        for a,b in edges:
            grap[a].add(b)
            grap[b].add(a)

        def get_hight(node):
            hight = 0
            for n in grap[node]:
                grap[n].remove(node)
                hight = max(hight, get_hight(n))
                grap[n].add(node)
            return hight+1
        
        min_hight = n+1
        nodes = []
        for i in range(n):
            hight = get_hight(i)
            if hight==min_hight:
                nodes.append(i)
            elif hight<min_hight:
                min_hight = hight
                nodes=[i]
        
        return nodes
