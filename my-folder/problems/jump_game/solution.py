class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        result = True
        goal = len(nums)-1
        
        if len(nums)==1:
            return True
        
        for i in range(len(nums)-1,-1,-1):
            
           
            
            if nums[i] >= goal - i:
                
                goal = i
                result=True
                
            else:
                result= False
            
            
        
        return result
            
        