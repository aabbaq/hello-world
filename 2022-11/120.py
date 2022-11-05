class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int: 
        l = len(triangle)
        dp = [[math.inf]*l for _ in range(l)]

        dp[0][0] = triangle[0][0]

        for i in range(1, l):
            for j in range(i+1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(dp[-1])