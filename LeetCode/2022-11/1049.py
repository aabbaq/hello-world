class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        _sum = sum(stones)
        n = len(stones)
        if n == 1: return stones[0]
        target = ceil(_sum / 2)

        dp = [[False] * (target+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        
        dp[0][stones[0]] = True

        for i in range(1, n):
            for j in range(1, target+1):
                if stones[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-stones[i]]

        for i in range(target, -1, -1):
            if dp[-1][i]:
                return abs(i - (_sum-i)) 