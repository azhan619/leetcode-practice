class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        while(left < right):
            
            area = ( right - left) * min(height[left],height[right])
            maxArea = max(maxArea,area)
            
            if height[left] > height[right]:
            
                right = right - 1
            
            else :
                
                left = left + 1
                
        return maxArea 
            