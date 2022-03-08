# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #print(list1)
        #print(list2)
        if list1==None:
            return list2
        if list2==None:
            return list1
        
        res=ListNode(0)
        ret_res=res
        while True:
            if list1.val==101 and list2.val==101:
                break
            if list1.val<=list2.val:
                res.next=ListNode(list1.val)
                list1=list1.next if list1.next!=None else ListNode(101)
            else:
                res.next=ListNode(list2.val)
                list2=list2.next if list2.next!=None else ListNode(101)
            res=res.next
            print(res)
        return ret_res.next
        