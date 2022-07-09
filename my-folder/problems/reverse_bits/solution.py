class Solution:
    def reverseBits(self, n: int) -> int:
        
        
        output = 0
        
        for i in range(32):
            
            output = output << 1
            
            curBit = n % 2
            
            output = output + curBit
            
            n = n >> 1
        
        
        
            
        return output     
            
        