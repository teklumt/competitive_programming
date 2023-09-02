# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        reserve=[]
        cur=head
        while cur:
            reserve.append(cur.val)
            cur=cur.next
        result=0
        n=len(reserve)
        for i in range((n//2)):
            gun=reserve[i]+reserve[n-1-i]
            if gun>result:
                result=gun
        return result