# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k==0:
            return head
        
        size=1
        cur=head
        while cur.next:
            cur=cur.next
            size+=1
        
        k=k%size
        if k==0:
            return head
        
        front=size-k
        cur=head
        for _ in range(front-1):
            cur=cur.next
        
        result=cur.next
        cur.next=None
        
        cur=result
        while cur.next:
            cur=cur.next
            
        cur.next=head
        
        return result
            
        
        
        
            