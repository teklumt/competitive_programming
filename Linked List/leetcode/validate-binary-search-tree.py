# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        global arr
        arr=[]
        def traversal(root):
            global arr
            if not root:
                return 
            traversal(root.left)
            arr.append(root.val)
            traversal(root.right)
            return arr
        arr=traversal(root)
        
        return arr==sorted(arr) and len(arr)==len(set(arr))   