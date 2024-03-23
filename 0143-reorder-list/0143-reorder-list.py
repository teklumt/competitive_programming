# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def reverse(node):
            pre = None
            cur = node
            while cur:
                tem = cur.next
                cur.next = pre
                pre = cur
                cur = tem
            return pre

        
        fast = slow = temp = head
        while fast and fast.next:
            temp  = slow
            slow = slow.next
            fast = fast.next.next

        temp.next  = None
        slow = reverse(slow)

        dummy = ListNode()
        cur = dummy
        
        while head and slow:
            cur.next = head
            cur = cur.next
            head = head.next

       
            cur.next = slow
            cur = cur.next
            slow = slow.next
            
     
        if slow:
            cur.next = slow
        if head:
            cur.next = head
        if cur.next:
            cur.next.next= None
    
   
        head = dummy.next


