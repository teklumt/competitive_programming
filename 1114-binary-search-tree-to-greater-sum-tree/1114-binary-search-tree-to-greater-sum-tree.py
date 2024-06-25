# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nums = []
        
        def inorder(root):
            if not root: return

            inorder(root.left)           
            nums.append(root.val)
            inorder(root.right)
        inorder(root)
        pre = list(accumulate(nums[::-1]))[::-1]
        def inorderModi(root):
            if not root :return
            inorderModi(root.left)
            root.val = pre[bisect_left(nums, root.val)]
            inorderModi(root.right) 
        inorderModi(root)

        return root          


        