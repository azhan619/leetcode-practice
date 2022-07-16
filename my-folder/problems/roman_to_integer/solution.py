class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        rom_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        i = 0
        j = 1
        output = 0
        
        while i < len(s) :
            
            if i < len(s)-1:
                
                if rom_dict[ s[i] ] < rom_dict[ s[i+1] ]:
                    
                    output = output +  ( int( rom_dict[s[i+1]] ) - int( rom_dict[s[i]])   )
                    i = i + 2
                
                else:
                    output = output +  int( rom_dict[s[i]])   
                    i = i + 1
          
            else:
                    output = output +  int( rom_dict[s[i]])   
                    i = i + 1                
                
            
        return output      