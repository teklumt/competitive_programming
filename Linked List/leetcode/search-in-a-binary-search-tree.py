# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        global ans
        ans=None
        def traversal(root):
            global ans
            if not root:
                return 
            if root.val==val:
                ans=root
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return ans