class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        val_1 = 0
        val_2 = 0
                
        val_3 = 0
        val_4 = 0
        j=0
        
        for k in nums:
            if j == len(nums)-1:
                break
            
            
            t = max(k+val_1,val_2)
            val_1 = val_2
            val_2 = t
            j=j+1
        
        t =0
        for k in nums:
            if t==0:
                t=1
                continue
            
            t = max(k+val_3,val_4)
            val_3 = val_4
            val_4 = t           
            
            
            
        
        
        
        return max(nums[0],val_2,val_4)
        