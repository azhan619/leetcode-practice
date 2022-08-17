# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None :
            
            return list2
        
        if list2 is None:
            
            return list1
        
        if list1.val > list2.val:
            resultList = ListNode(list2.val)
            list2 = list2.next
            head = resultList
        else:
            resultList = ListNode(list1.val)
            list1 = list1.next
            head = resultList
        
        while list1 is not None and list2 is not None:
            
            
            
            if (list1.val > list2.val ):
                resultList.next = ListNode(list2.val)
                list2 = list2.next
            else:
                resultList.next = ListNode(list1.val)
                list1 = list1.next
            resultList = resultList.next
            
        while list1 is not None:
            resultList.next = ListNode(list1.val)
            list1 = list1.next
            resultList = resultList.next
        while list2 is not None:
            resultList.next = ListNode(list2.val)
            list2 = list2.next
            resultList = resultList.next 
            
            
        return head    
        