class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+','', s)
        s = s.lower()
        
        #print(s)
        
        i = 0
        j = len(s)- 1
       
        while(i <= j):
            
            if(s[i] != s[j]):
                
                
                if(self.checkPalindrome(s,i,j-1)):
                    return True
                if(self.checkPalindrome(s,i+1,j)):
                    return True
                
                
                return False
                
                
                
            i += 1
            j -= 1
        return True      
    def checkPalindrome(self,s:str,i,j):
        
        i = i
        j = j
        
        
        
        
        
        while(i <= j):
            
            if(s[i] != s[j]):
                
                return False
                
                
                
            i += 1
            j -= 1
        return True  