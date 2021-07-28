class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c):
            # check boundary
            if not (0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])):
                return 0
            
            #basecase
            if grid[r][c] == 0:
                return 0
            
            # check if visited
            if grid[r][c] == '?':
                return 0
            
            # marking (r,c) as visited
            temp = grid[r][c]
            grid[r][c] = '?'
            
            left_path = temp + dfs(grid, r, c-1)
            right_path = temp + dfs(grid, r, c+1)
            top_path = temp + dfs(grid, r+1, c)
            down_path = temp + dfs(grid, r-1, c)
            
            grid[r][c] = temp
            
            return max(left_path, right_path, top_path, down_path)
            
        max_gold = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                max_gold = max(max_gold, dfs(grid, r, c))
        
        return max_gold