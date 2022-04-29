# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        start= None
        
        while head.next is not None:
            tmp = head.next
            
            head.next=start
            start=head
            head = tmp
            
        head.next = start
        
        return head
