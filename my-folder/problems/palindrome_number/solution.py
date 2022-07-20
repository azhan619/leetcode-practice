class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        int_st = str(x)
        
        i = 0
        j = len(int_st) - 1
        
        result = True
        
        while i <= j :
            
            if int_st[i] != int_st[j]:
                result = False
            i = i + 1
            j = j - 1
            
            
        
        
        return result