class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 1:
            if nums[0] == target or nums[0] == -target:
                return 1
            else:
                return 0
        
        pos2 = target + sum(nums)
        pos = pos2 >> 1
        if pos << 1 != pos2: return 0

        dp = [[0] * (pos+1) for _ in range(n)]    
        for i in range(n):
            dp[i][0] = 1

        dp[0][nums[0]] = 2 if nums[0] == 0 else 1

        for i in range(1, n):
            for j in range(pos+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]

        return dp[-1][-1]