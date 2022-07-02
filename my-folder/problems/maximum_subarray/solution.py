class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        
        maxSub = nums[0]
        
        curSum = 0
        
        for k in nums:
            
            if curSum < 0:
                curSum = 0
                
            curSum = curSum + k
            maxSub = max(maxSub,curSum)
        
        return maxSub