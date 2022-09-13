class Solution:
    def isValid(self, s: str) -> bool:
        
        
        paraStack = []
        
        paraMap = {
            ')':'('
            ,'}':'{'
            ,']':'['
        }
        
        for i in s:
            
            if i in paraMap:
                if paraStack and paraStack[-1] == paraMap[i]:
                    paraStack.pop()
                else:
                    return False
            else:
                paraStack.append(i)
        
                
        
        return False if paraStack else True