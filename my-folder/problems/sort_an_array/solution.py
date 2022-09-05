class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        if (len(nums) == 1) :
            
            return nums
        
        
        mid = len(nums) // 2
        
        left = nums[:mid]
        right = nums[mid:]
        
        
        return self.merge(self.sortArray(left),self.sortArray(right))
    
    def merge(self,left,right):
        
        result = []
        
        l = 0
       
        r = 0
        
        while(l < len(left) and r < len(right)):
            
            if(left[l] <= right[r]):
                
                
                result.append(left[l]) 
                l = l + 1
            
            else:
                result.append(right[r])
                r = r+1
        while (l < len(left)):
                result.append(left[l]) 
                l = l + 1
        while (r< len(right)):
                result.append(right[r])
                r = r+1
        return result
            
        