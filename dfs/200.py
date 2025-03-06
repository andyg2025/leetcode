class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        seen = [[False]*m for _ in range(n)]
        result = 0

        def dfs(x, y):
            if x<n and x>=0 and y<m and y>=0 and grid[x][y]=="1" and not seen[x][y]:
                seen[x][y] = True
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and not seen[i][j]:
                    result+=1
                    dfs(i, j)
        
        return result