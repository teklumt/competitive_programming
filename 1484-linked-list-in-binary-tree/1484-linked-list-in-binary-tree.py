# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfs(root, curNode):
            if not curNode:  
                return True
            if not root:  
                return False
            if curNode.val == root.val:  
                if dfs(root.left, curNode.next) or dfs(root.right, curNode.next):
                    return True
            return False
        
        if not root:return False
        if dfs(root, head):return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)