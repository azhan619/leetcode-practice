class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left = len(nums)-1
        right = 0
        leftSum = 0
        rightSum = 0
        total =0
        
        for i in nums:
            total = total + i
            
        
        st=0
        index=0
        for k in range(len(nums)):
            
            total = total - nums[k]
            
            if total == st:
            
                return k
            
            st = st + nums[k]
        return -1
            
            
            
            
            
        