class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = max(nums)
        
        curMin = 1
        curMax = 1
        
        for k in nums:
            
            if k == 0:
                curMin = 1
                curMax = 1
                continue
                
            temp = curMax * k   
                
            curMax = max(k*curMax,k*curMin,k)
            
            curMin = min(temp,k*curMin,k)
            
            result = max(result,curMin,curMax)
            
        
        return result
            
            
                
               
        