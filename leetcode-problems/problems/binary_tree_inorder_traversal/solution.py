# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if(root == None):
            return 
        self.traverse(root,result)
        return result
        
    def traverse(self,root,result):
        
        if(root.left):
            self.traverse(root.left,result)
        result.append(root.val)
        if(root.right):
            self.traverse(root.right,result)
        
             
        