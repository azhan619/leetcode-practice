class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        left = 0
        right = len(numbers) - 1
        result = []
        
        while left <= right:
        
            if numbers[left] + numbers[right] == target:
                result.append( left + 1 )
                result.append( right + 1 )
                return result
            
            elif numbers[left] + numbers[right] > target:
            
                right = right - 1
                
            else:
                left = left + 1