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

        res = [target.val]
        for _ in range(k):
            print(res)
            new_res = []
            for val in res:
                if val not in seen:
                    seen.add(val)
                    for node in graph[val]:
                        if node not in seen:
                            new_res.append(node)

            res[:]=new_res[:]
        
        return res
                

        return res
