# better than before, but also Time Limit Exceeded

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        grap = [set() for _ in range(n)]
        for a,b in edges:
            grap[a].add(b)
            grap[b].add(a)

        memory = {}

        def get_hight(node):
            hight = 0
            for n in grap[node]:
                cur_hight = 0
                if (node, n) in memory:
                    cur_hight =  memory[(node, n)]
                else:
                    grap[n].remove(node)
                    cur_hight = get_hight(n)
                    memory[(node, n)] = cur_hight
                    grap[n].add(node)
                hight = max(hight, cur_hight)
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