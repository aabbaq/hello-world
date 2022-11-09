class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        
        grid = [[1]*n for _ in range(n)]
        dp = [[[1]*4 for _ in range(n)] for _ in range(n)]
        res = [0] * n * n
        for x,y in mines:
            grid[x][y] = 0
            dp[x][y][0] = 0
            dp[x][y][1] = 0
            dp[x][y][2] = 0
            dp[x][y][3] = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    if i > 0 and grid[i-1][j] == 1:
                        dp[i][j][0] = dp[i-1][j][0] + 1
                    if j > 0 and grid[i][j-1] == 1:
                        dp[i][j][2] = dp[i][j-1][2] + 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] != 0:
                    if i < n-1 and grid[i+1][j] == 1:
                        dp[i][j][1] = dp[i+1][j][1] + 1
                    if j < n-1 and grid[i][j+1] == 1:
                        dp[i][j][3] = dp[i][j+1][3] + 1
                    res[i*n+j] = min(dp[i][j])

        return max(res)
