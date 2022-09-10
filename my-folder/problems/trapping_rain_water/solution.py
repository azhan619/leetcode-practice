class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = 0
        maxRight = 0
        
        l = 0
        r = len(height) - 1
        total = 0
        
        while (r > l):
            
            if(height[r] <= height[l]):
                
                if(height[r] <= maxLeft):
                    
                    curTrap = maxLeft - height[r]
                    print(str(curTrap))
                    
                    if ( curTrap > 0 ):
                        total = total + curTrap
                
                    
                else: 
                    maxLeft = height[r]
                r -= 1
            else:
                
                if(height[l] <= maxRight):
                    
                    curTrap = maxRight - height[l]
                    print(str(curTrap))
                    if (curTrap > 0):
                        total = total + curTrap
                   
                    
                else: 
                    maxRight = height[l]
                l += 1    
                
       
        return total  
      
        