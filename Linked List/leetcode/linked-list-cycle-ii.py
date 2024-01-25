# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left=head
        seen=set()
        while left:
            seen.add(left)
            left=left.next
            if left in seen:
                return left
        return None
        