class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        preReq = {i:[] for i in range(numCourses)}
        
        
        visitSet = {}
        
        for a,b in prerequisites:
            preReq[a].append(b)
        visitedNode = set()
        
        def dfs(node):
            
            if node in visitedNode:
                return False
            if preReq[node] == []:
                return True
            
            visitedNode.add(node)
            
            for i in preReq[node]:
                if not dfs(i):
           
                    return False
            visitedNode.remove(node)
            
            preReq[node] = [] 
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True     
                  