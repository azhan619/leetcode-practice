class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        
        def recursive_dfs(i,current,total):
            
            if total == target:
                
                output.append(current.copy())
                return
         
            
            if i >= len(candidates) or total > target:
                return
            
            current.append(candidates[i])
            
            recursive_dfs(i,current,total + candidates[i])
            
            current.pop()
            
            recursive_dfs(i+1,current,total)
       
        recursive_dfs(0,[],0)
        return output
            