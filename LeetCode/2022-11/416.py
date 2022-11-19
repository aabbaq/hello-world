class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        _sum = sum(nums)
        target = _sum // 2

        if target * 2 != _sum: return False

        dp = [[False] * (target+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        for i in range(1, n):
            for j in range(1, target+1):
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]