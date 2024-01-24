# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            target=None
            while head:
                cur=head.next
                head.next=target
                target=head
                head=cur
            return target
        
        cur=head
        n=0
        while cur:
            cur=cur.next
            n+=1
        mid=n//2
        left=right=head
        n=0
        while n<mid:
            right=right.next
            n=n+1
        right=reverse(right)
        
        while left and right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True
        
        