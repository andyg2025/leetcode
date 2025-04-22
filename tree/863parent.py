# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def addParent(cur, parent):
            if cur:
                cur.parent = parent
                addParent(cur.left, cur)
                addParent(cur.right, cur)
        
        addParent(root, None)

        res=[]
        seen=set()
        def dfs(node, distance):
            if not node or node in seen:
                return
            
            seen.add(node)
            
            if distance==0:
                res.append(node.val)
                return
            
            dfs(node.left, distance-1)
            dfs(node.right, distance-1)
            dfs(node.parent, distance-1)

        dfs(target, k)
        return res