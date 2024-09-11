# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        currD = dummy
        while head.next:
            temp = head.next
            currD.next = head
            currD = currD.next
            currD.next = ListNode(gcd(head.val, head.next.val))
            currD = currD.next
            head = temp
        if head:
            currD.next = head
        return dummy.next