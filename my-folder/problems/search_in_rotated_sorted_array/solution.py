class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        
        left = 0
        right = len(nums)-1
        
        
        
        
        
        while left <= right:
        
            middle = left + (right - left) // 2
            
            if nums[middle] == target:
                result = middle
                break
           
            
            if nums[middle] >= nums[left]:
                if nums[left] > target:
                    left = middle + 1
               
                elif nums[middle] < target:
                    left = middle + 1
            
                else:
                    right = middle - 1
            #right portion        
            else:
                
                if nums[right] < target:
                    right = middle - 1
                 
                elif nums[middle] > target:
                    right = middle -1
               
                else:
                    left = middle + 1
                    
                    
                    
        return result
        
        
        
        