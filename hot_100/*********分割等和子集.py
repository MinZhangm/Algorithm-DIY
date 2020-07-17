class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = int(target/2)
        dp = [[False for _ in range(target+1)] for _ in range(n)]
        if not nums:
            return True
        dp[0][0] = True

        for i in range(1, target+1):
            if nums[0] == i:
                dp[0][i] = True

        for i in range(1, n):
            for j in range(target+1):
                if j > nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
