class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        maxDiff = -1
        k=0
        minElem = nums[0]
        lent = len(nums)
        for i, item in enumerate(nums):
           
            
           
        
            
            if item < minElem:
                
                minElem = item
                print(minElem)
           
            if item > minElem:
                diff = item - minElem
                maxDiff = max(diff,maxDiff)
                
        
        return maxDiff
                 
        