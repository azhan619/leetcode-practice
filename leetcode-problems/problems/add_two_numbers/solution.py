# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(0)
        
        currentNode = dummyNode
        
        carry = 0
        
        while l1 != None or l2 != None or carry !=0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            total = l1Val + l2Val + carry
            
            carry = total // 10
            
            Node = ListNode(total %10)
            
            currentNode.next = Node
            
            currentNode = Node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummyNode.next
            
            
            
            
        