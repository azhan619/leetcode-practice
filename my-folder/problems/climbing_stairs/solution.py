class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        
        memo = []
        memo = [0 for i in range(0,n+1)]
        memo[0] = 1
        memo[1] = 1
        
        for x in range(2,n+1):
            memo[x] = memo[x-1] + memo[x-2]
            
        
        return memo[n]
        