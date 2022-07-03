class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        target=0
        total=0
        
        for i in range(0,len(nums)+1):
            target = target + i
            
        for k in nums:
            total = total + k
            
       
    
    
        return target - total
            
            