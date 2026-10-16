# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD=0
        #d = max(self.depth(root.left), self.depth(root.right))
        # longest distance between a shared root
        def depth(node):
            nonlocal maxD

            if node == None:
                return 0
            else:
                leftHeight = depth(node.left)
                rightHeight = depth(node.right)
                maxD = max(maxD, leftHeight+ rightHeight)
                return 1+max(leftHeight, rightHeight)

        depth(root)
        return maxD

    
        #return maxD



