class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        roots = {}
        leaves = set()

        def find_root(node):
            while roots[node] != node:
                node = roots[node]
            return node

        for i in range(n):
            roots[i] = i
            leaves.add(i)

        for t, x, y in logs:
            root = find_root(x)
            new_root = find_root(y)
            if root == new_root:
                continue
            roots[root] = new_root
            leaves.remove(root)

            if len(leaves) == 1:
                return t
        
        return -1
