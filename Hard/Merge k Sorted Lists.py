# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        while len(lists) > 1:
            merged=[]
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                merged.append( self.mergeTwoLists(l1,l2) )
                
            lists=merged
            
        return lists[0]
            
        
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
