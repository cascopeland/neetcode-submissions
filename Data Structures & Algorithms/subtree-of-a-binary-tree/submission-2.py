# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(r, subR):
            if not r and not subR:
                return True
            if not r or not subR:
                return False
            if r.val != subR.val:
                return False
            return dfs(r.left, subR.left) and dfs(r.right, subR.right)
        if not subRoot:
            return True
        if not root:
            return False
        if dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
