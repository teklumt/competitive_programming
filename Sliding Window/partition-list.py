# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        dummyLess=ListNode()
        dummyGreater=ListNode()
        
        curLess=dummyLess
        curGreater=dummyGreater
        cur=head
        
        while cur:
            if cur.val<x:
                curLess.next=cur
                curLess=curLess.next
            else:
                curGreater.next=cur
                curGreater=curGreater.next
            cur=cur.next
            
        curLess.next=dummyGreater.next
        curGreater.next=None
        
        return dummyLess.next