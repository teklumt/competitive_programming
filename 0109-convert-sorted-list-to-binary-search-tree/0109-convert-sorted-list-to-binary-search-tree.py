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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if head.next == None:
            return TreeNode(head.val)

        def findMid(head):
            fast = slow = pre = head

            while fast and fast.next:
                fast = fast.next.next
                pre = slow
                slow = slow.next
            if pre:
                pre.next = None
            return slow
        
        mid = findMid(head)
        return TreeNode(mid.val, self.sortedListToBST(head), self.sortedListToBST(mid.next) )


        

        
        