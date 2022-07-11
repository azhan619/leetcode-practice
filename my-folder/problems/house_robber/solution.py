class Solution:
    def rob(self, nums: List[int]) -> int:
        
        val_1 = 0
        
        val_2 = 0
        
        for k in nums:
            
            t = max(k + val_1,val_2)
            val_1 = val_2
            val_2 = t
            
        
        return val_2
            
        