class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        
        q = deque()
        
        time = 0
        fresh = 0
        
        ROW = len(grid)
        COLUMN = len(grid[0])
        
        for r in range(ROW):
            
            for c in range(COLUMN):
                
                if grid[r][c] == 1:
                    fresh = fresh + 1
                if grid[r][c] == 2:
                    q.append([r,c])
                    
        direct = [ [0,1],[1,0],[-1,0],[0,-1]  ]             
        
        while q and fresh > 0:
           
            
            for i in range(len(q)):
                
                r,c = q.popleft()
                
                for a,b in direct:
                    
                    newr,newc = r + a , c + b
                    
                    if ( newr < 0 or newr == len(grid) or newc<0 or newc == len(grid[0]) or
                        grid[newr][newc] != 1
                       ):
                        
                        continue
                        
                    grid[newr][newc] = 2
                    q.append([newr,newc])
                    fresh = fresh - 1
                    print(fresh)
            time = time + 1
            
                
        if fresh == 0:
            return time
        else:
            return -1
                
            
                    