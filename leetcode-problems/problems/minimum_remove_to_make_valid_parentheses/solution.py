class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        
        i = 0
        brackStack = []
        
        while(i < len(s)):
            #print(s[i])
            
            if (s[i] == '('):
                brackStack.append(i)
                 
            if ( s[i] == ')' ):
                
                if(len(brackStack) == 0):
                    s = s[:i] + s[i + 1:]
                    i -= 1
                    #print(s + 'with i : ' + str(i))
                    
                else:   
                    brackStack.pop()
            i += 1
        
        
        while(brackStack):
            j = brackStack.pop()
            s = s[:j] + s[j + 1:]
            
        return s    
            
            