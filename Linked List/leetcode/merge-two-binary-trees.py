# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merge(root1,root2):
          
                
            if  root1 and root2:
                root1.val+=root2.val
                root1.left=merge(root1.left,root2.left)
                root1.right=merge(root1.right,root2.right)

            return root1 if root1 else root2

        
        return merge(root1,root2)
