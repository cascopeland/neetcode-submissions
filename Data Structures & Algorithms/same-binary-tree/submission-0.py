# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root_q, root_p):
            if not root_q and not root_p:
                return True
            if not root_q or not root_p:
                return False
            if root_p.val != root_q.val:
                return False
            
            return dfs(root_q.left, root_p.left) and dfs(root_q.right, root_p.right)
        return dfs(q, p)