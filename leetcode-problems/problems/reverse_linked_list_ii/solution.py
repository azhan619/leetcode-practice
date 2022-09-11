# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        start = head
        
        
        pos = 1
        curNode = head
        
        
        
        while(pos < left):
            
            start = curNode
            curNode = curNode.next
            pos += 1
       
        newList = None
        tail = curNode
        
        while(pos >= left and pos <= right):
            
            nextNode = curNode.next
            curNode.next = newList
            newList = curNode
            curNode = nextNode
            pos += 1
                
        start.next = newList
        tail.next = curNode
        
        if(left > 1):
            return head
        else:
            return newList
            
        