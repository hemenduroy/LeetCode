# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        head=res
        while list1 or list2:
            if list1 is None:
                res.next=list2
                break
            
            if list2 is None:
                res.next=list1
                break
                
            if list1.val<=list2.val:
                node=ListNode(list1.val)
                list1=list1.next
            else:
                node=ListNode(list2.val)
                list2=list2.next
                
                
            res.next=node
            res=res.next
            
        #print(list1,list2)
            
        return head.next
