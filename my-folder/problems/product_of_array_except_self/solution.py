class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * (len(nums))
        
        prefix = 1
        postfix =1
        
        for i in range(len(nums)):
            
            output[i] = prefix
            
            prefix = prefix * nums[i]
            
        lnth = len(nums)-1
        print(output)
        for k in range(len(nums)):
            
            
            output[lnth] = output[lnth] * postfix
            postfix = nums[lnth]*postfix
            lnth = lnth -1
        
        return output
            