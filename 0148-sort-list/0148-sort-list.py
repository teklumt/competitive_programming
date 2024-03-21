# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        def mid(head):
            slow, fast = head,head
            temp = slow
            while fast and fast.next:
                temp = slow
                slow = slow.next
                fast = fast.next.next
            
            temp.next = None if temp else temp
            return slow
        
        def merge(head1, head2):
            dummy = ListNode()
            curr = dummy
            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = head1
                    
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next

                curr = curr.next
            if head1:
                curr.next = head1
            if head2:
                curr.next = head2
            return dummy.next
        
       
        def mergeSort(head):
            if not head or not head.next:
                return head
            mi = mid(head)
            left = mergeSort(head)
            right = mergeSort(mi)
            return merge(left, right)
        return mergeSort(head)
        
        
            
            
            
            
            
            
            
            
            