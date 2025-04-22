# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        graph[root.val] = []
        def get_graph(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val] = [node.val]
                get_graph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val] = [node.val]
                get_graph(node.right)

        get_graph(root)

        seen = set()
        res = []

        def dfs(val, k):
            if val in seen:
                return
            
            seen.add(val)

            nexts = graph[val]
            if not nexts:
                return
            
            if k==0:
                res.append(val)
                return

            for nodeval in nexts:
                dfs(nodeval, k-1)

        dfs(target.val, k)

        return res
