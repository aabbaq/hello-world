class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(l+1)]

        for i in range(1, l+1):
            c0 = strs[i-1].count('0')
            c1 = strs[i-1].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    if j < c0 or k < c1:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-c0][k-c1] + 1)

        return dp[-1][-1][-1]