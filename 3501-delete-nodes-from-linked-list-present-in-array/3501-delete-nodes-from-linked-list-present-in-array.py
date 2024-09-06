# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curD = dummy

        nums = set(nums)
        while head:
            if head.val not in nums:
                curD.next = head
                curD = curD.next
            head = head.next
        curD.next = None
        return dummy.next