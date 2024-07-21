# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy

        temp = 0
        while head:
            if head.val != 0:
                temp += head.val
            else:
                if temp:
                    res.next = ListNode(temp)
                    res = res.next
                    temp = 0
            head = head.next
        return dummy.next 
        