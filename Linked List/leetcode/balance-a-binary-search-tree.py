# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(root):
            nonlocal nums
            if not root: return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        inorder(root)
        def createTree(num):
            if not num:return
            mid = len(num) // 2
            return TreeNode(num[mid], createTree(num[:mid]), createTree(num[mid + 1: ]))
        return createTree(nums)

            
        