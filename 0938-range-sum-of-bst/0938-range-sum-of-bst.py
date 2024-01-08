# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        global res
        res = 0


        def traversal(root):

            global res
            if root is None:
                return 0
            traversal(root.left)
            if low <= root.val <= high:
                res += root.val
            traversal(root.right)


        traversal(root)
        return res

                