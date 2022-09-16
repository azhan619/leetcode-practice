class Solution:
    def mySqrt(self, x: int) -> int:
        
        if( x == 1):
            return 1
        if(x ==0):
            return 0
        
        result = 1
        i = 1
        
        while(result <= x):
            i += 1
            result = i*i
           
            
        return i -1     
            
            
        