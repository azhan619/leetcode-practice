"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curNode = head
        
        while( curNode != None ):
            
            if(curNode.child != None):
                nextNode = curNode.next
                start = curNode
                childHead = curNode.child
                newCurNode = curNode.child
                
                endNode = newCurNode
                
                while(newCurNode!= None ):
                
                    endNode = newCurNode
                    newCurNode = newCurNode.next
                    
                print(str(endNode.val))   
                if( nextNode != None):
                    nextNode.prev = endNode
                
                endNode.next = nextNode
                childHead.prev = start
                
                start.child = None
                start.next = childHead
            curNode = curNode.next           
        return head            
                    
                    
                    
                
            
        