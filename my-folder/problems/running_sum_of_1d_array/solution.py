class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        
        
        
        for k in range(len(nums)-1):
            
            nums[k+1] = nums[k] + nums[k+1]
        
        
        
        return nums    